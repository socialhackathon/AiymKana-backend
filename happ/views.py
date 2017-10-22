from .models import *
from .serializers import *
from .permisions import *

from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken


class FriendList(generics.ListCreateAPIView):
    serializer_class = FriendSerializer
    queryset = Friend.objects.all()
    # need to implement authentification -----
    # permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     qset = Friend.objects.filter(contact=self.request.user)
    #     return qset


class FriendDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FriendSerializer
    # permission_classes = (IsAuthenticated, IsOwner)
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


'''
class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print(request.user)
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
