from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, name, phone_number, password=None):
        if not email:
            raise ValueError("The Email field is required")
        
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone_number, password=None):
        user = self.create_user(
            email=email,
            name=name,
            phone_number=phone_number,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    

class Visitor(AbstractBaseUser):
    name = models.CharField(max_length=50, null=False)
    phone_number = models.CharField(max_length=50, null=False)
    email = models.EmailField(unique=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_number']
    
    def __str__(self) -> str:
        return self.name
    
    def visited_residents(self):
        from resident.models import Resident
        return Resident.objects.filter(residentvisitor__visitor=self)
