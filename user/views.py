from django.shortcuts import render

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework import generics, mixins


class UserDetailByIdView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
