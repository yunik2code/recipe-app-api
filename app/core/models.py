"""
Applicatipn models
"""
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, 
    PermissionsMixin,
    AbstractBaseUser,
)

class UserManager(BaseUserManager):
    """Custom User Mdoel manager that creates , saves and return a new user

    Args:
        BaseUserManager (Class): Base class that manages custom user
    """
    def create_user(self, email, password=None, **extra_fields):
        """Creates , saves and returns a new user

        Args:
            email (email): Email of the user
            password (password, optional): password of the user. Defaults to None.
        """
        if not email:
            raise ValueError('Email name must be provided')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates , saves and returns a superuser/admin

        Args:
            email (str): Email of the superuser
            password (str): Password of the superuser
        """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user



class User(AbstractBaseUser, PermissionsMixin):
    """Custom USer class

    Args:
        BaseUserManager (class): Base class that contains Authentication mechanism
        PermissionsMixin (class): Base class that contains permissions and fileds
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = UserManager()