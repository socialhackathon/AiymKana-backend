from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hell, worl")
