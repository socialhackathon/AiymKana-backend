from django.contrib import admin
from .models import *


# Register your models here.

class EmergencyServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'phone_1')


class EmergencyServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'description')


class FriendAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'profile')
    list_filter = ['profile', ]


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number')


class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'profileNum')
    list_filter = ['profileNum', ]


class PinAdmin(admin.ModelAdmin):
    list_display = ('info', 'id', 'latitude', 'longitude')


class InformationAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'image_url', 'last_updated')


admin.site.register(EmergencyService, EmergencyServiceAdmin)
admin.site.register(EmergencyServiceCategory, EmergencyServiceCategoryAdmin)
admin.site.register(Friend, FriendAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Story, StoryAdmin)
admin.site.register(Pin, PinAdmin)
admin.site.register(Information, InformationAdmin)
