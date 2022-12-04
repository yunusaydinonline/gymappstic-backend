"""
DB Models implemented with Django ORM
"""
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.utils.translation import gettext_lazy as t
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, email, password, **kwargs):
        """Create and return saved user"""

        if not username:
            raise ValueError(t('Username must not be empty or None'))
        elif not email:
            raise ValueError(t('Email must not be empty or None'))
        elif not password:
            raise ValueError(t('Password must not be empty or None'))

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password, **kwargs):
        """Create and return saved super user"""

        user = self.create_user(username, email, password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

    def create_apiuser(self, username, email, password, **kwargs):
        """Create and return saved API user"""

        user = self.create_user(username, email, password, **kwargs)
        user.is_apiuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User model"""
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_apiuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f'{self.username}'
