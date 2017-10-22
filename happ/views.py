from .serializers import *
from .permisions import *

from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken


class FriendList(generics.ListCreateAPIView):
    serializer_class = FriendSerializer
    queryset = Friend.objects.all()


class FriendDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FriendSerializer
    queryset = Friend.objects.all()


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile"""

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_field = ('first_name', 'last_name',)


class LoginViewSet(viewsets.ViewSet):
    """Checks email and password `and returns an auth token"""
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to obtain and create a token"""
        return ObtainAuthToken().post(request)


class ServiceList(generics.ListAPIView):
    queryset = EmergencyService.objects.all()
    serializer_class = EmergencyServiceSerializer


class ServiceDetail(generics.RetrieveAPIView):
    queryset = EmergencyService.objects.all()
    serializer_class = EmergencyServiceSerializer


class EmergencyServiceCategoryList(generics.ListAPIView):
    queryset = EmergencyServiceCategory.objects.all()
    serializer_class = EmergencyServiceCategorySerializer


class EmergencyServiceCategoryDetail(generics.RetrieveAPIView):
    queryset = EmergencyServiceCategory.objects.all()
    serializer_class = EmergencyServiceCategorySerializer


class ServicesByCategoryList(generics.ListAPIView):
    serializer_class = EmergencyServiceSerializer

    def get_queryset(self):
        cat = get_object_or_404(EmergencyServiceCategory, pk=self.kwargs['pk'])
        qset = EmergencyService.objects.filter(category=cat)
        return qset


class FriendsByProfileList(generics.ListAPIView):
    serializer_class = FriendSerializer

    def get_queryset(self):
        con = get_object_or_404(UserProfile, pk=self.kwargs['pk'])
        qset = Friend.objects.filter(profile=con)
        return qset


class StoryList(generics.ListCreateAPIView):
    serializer_class = StorySerializer
    queryset = Story.objects.all()


class StoryDetail(generics.RetrieveAPIView):
    serializer_class = StorySerializer
    queryset = Story.objects.all()


class PinList(generics.ListCreateAPIView):
    serializer_class = PinSerializer
    queryset = Pin.objects.all()


class PinDetail(generics.RetrieveAPIView):
    serializer_class = PinSerializer
    queryset = Pin.objects.all()


class InformationList(generics.ListCreateAPIView):
    serializer_class = InformationSerializer
    queryset = Information.objects.all()


class InformationDetail(generics.RetrieveAPIView):
    serializer_class = InformationSerializer
    queryset = Information.objects.all()
