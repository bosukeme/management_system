from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth import authenticate

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

from drf_spectacular.utils import extend_schema

from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import PortalUserRegistrationSerializer, PortalUserLoginSerializer

@extend_schema(tags=['PortalUser-auth'])
class PortalUserViewSet(viewsets.ViewSet):
    
    def get_serializer_class(self):
        if self.action == 'register':
            return PortalUserRegistrationSerializer
        elif self.action == 'login':
            return PortalUserLoginSerializer
        # Return a default serializer or None
        return None

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = PortalUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": f'User {user.name} created successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = PortalUserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['email']
            password = serializer.validated_data['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                }, status=status.HTTP_200_OK)
                
            else:
                print(f"Authentication failed for user {username}")
                return Response({'error': 'Invalid login credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        else:
            print("Serializer errors: ", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        try:
            refresh_token = request.data.get('refresh')
            if not refresh_token:
                return Response({'error': 'Refresh token is required.'}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                token = RefreshToken(refresh_token)
                # Blacklist the refresh token
                token.blacklist()
                return Response({'message': 'Logged out successfully.'}, status=status.HTTP_205_RESET_CONTENT)
            except Exception as e:
                print(f"Error blacklisting token: {e}")
                return Response({'error': 'Invalid or expired refresh token.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"Error during logout: {e}")
            return Response({'error': 'An error occurred during logout.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
            if user.check_password(password):
                return user
            else:
                print(f"Password mismatch for {username}")
        except UserModel.DoesNotExist:
            print(f"User with email {username} does not exist")
        return None
