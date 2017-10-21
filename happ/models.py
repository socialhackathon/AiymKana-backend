from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """Helps django with our custom user"""

    def create_user(self, phone_number, first_name, last_name, is_male, password=None):
        """Creates new user"""

        if not phone_number:
            raise ValueError('User must have phone number')

        user = self.model(phone_number=phone_number, first_name=first_name, last_name=last_name, is_male=is_male)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone_number, first_name, last_name, is_male, password=None):
        """Creates new superuser"""

        user = self.create_user(phone_number, first_name, last_name, is_male, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a user profile"""

    def get_full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.first_name

    phone_number = models.CharField(max_length=13, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_male = models.BooleanField(default=False)  # по дефолту в поле стоит "Ж"
    email = models.CharField(max_length=100, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'is_male']


class EmergencyService(models.Model):
    name = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    phone = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Friend(models.Model):
    name = models.CharField(max_length=225)
    phone = models.CharField(max_length=225)
    contact = models.ForeignKey(UserProfile, related_name='contacts', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
