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
    email = models.CharField(max_length=100, null=True)
    message_text = models.CharField(max_length=300, default='SOS')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'is_male']

class EmergencyServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'emergency service categories'


class EmergencyService(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300, null=True)
    latitude = models.CharField(max_length=30, null=True, blank=True)
    longitude = models.CharField(max_length=30,null=True, blank=True)
    phone_1 = models.CharField(max_length=100, null=True, blank=True)
    phone_2 = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    website = models.CharField(max_length=200, null=True, blank=True)

    category = models.ForeignKey(EmergencyServiceCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Friend(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    phone = models.CharField(max_length=225)
    email = models.CharField(max_length=225, null=True, blank=True)
    profile = models.ForeignKey(UserProfile, related_name='contacts', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'contact'

    def __str__(self):
        return self.name


class Story(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    timeAdded = models.DateTimeField(auto_now_add=True)

    profileNum = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'stories'

    def __str__(self):
        return self.title

class Pin(models.Model):
    info = models.CharField(max_length=300)
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Longitude: {} Latitude {}'.format(self.longitude, self.latitude)

class Information(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.URLField()
    body = models.TextField()
    last_updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'information'

    def __str__(self):
        return self.title
