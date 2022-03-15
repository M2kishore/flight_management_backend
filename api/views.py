from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializer import UserSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer