from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import *


class EmergencyServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyService
        fields = ( 'id', 'name', 'category', 'phone_1', 'address', 'latitude', 'longitude', 'phone_2', 'description', 'website')


class EmergencyServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyServiceCategory
        fields = ('id', 'name', 'description')


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ('id', 'name', 'phone', 'email', 'profile')

    def create(self, validated_data):
        # contact = self.context['request'].user
        contact = UserProfile.objects.first()
        validated_data['profile'] = contact
        return super().create(validated_data)


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('id', 'title', 'body', 'timeAdded', 'profileNum')


class PinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pin
        fields = ('info', 'id', 'latitude', 'longitude', 'added_at')


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ('title', 'id', 'image_url', 'body', 'last_updated')


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our UserProfile model"""

    class Meta:
        model = UserProfile
        fields = ('id', 'phone_number', 'first_name', 'last_name', 'password', 'email', 'message_text')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user"""

        user = UserProfile(
            phone_number=validated_data['phone_number'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_male=validated_data['is_male'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])

        user.save()

        return user

# class PersonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Person
#         fields = ('id', 'username', 'first_name', 'last_name', 'middlename', 'email', 'phone')
