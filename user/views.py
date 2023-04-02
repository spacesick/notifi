from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework import generics, mixins

from django.contrib.auth.views import LoginView, LogoutView

from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm

from django.views import View


# class UserDetailByIdView(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAdminUser]


# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAdminUser]


# class UserCreateView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('listings') 

class UserLogoutView(LogoutView):
    template_name = 'logout.html'

    def get_success_url(self):
        return reverse_lazy('login') 

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect('/login/')
    
class UserRegisterView(View):
    form_class = UserCreationForm
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = form.save(commit=True)

            return HttpResponseRedirect('/')

        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    