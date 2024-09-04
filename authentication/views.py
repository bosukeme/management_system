from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth import authenticate

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

from drf_spectacular.utils import extend_schema

from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import  VisitorRegistrationSerializer, VisitorLoginSerializer, VisitorSerializer


@extend_schema(tags=['visitors-auth'])
class VisitorViewSet(viewsets.ViewSet):
    
    def get_serializer_class(self):
        if self.action == 'register':
            return VisitorRegistrationSerializer
        elif self.action == 'login':
            return VisitorLoginSerializer
        return super().get_serializer_class()

    
    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = VisitorRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": f'User {user.name} created successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = VisitorLoginSerializer(data=request.data)
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

