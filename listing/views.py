from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Listing
from django.shortcuts import get_object_or_404
from .serializers import ListingSerializer
from .forms import ListingForm
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from rest_framework import generics, mixins

from django.views import View
from django.views.generic import ListView, DetailView


from django.contrib.auth.mixins import LoginRequiredMixin


class ListingsView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'listings.html'
    # model = Listing

    def get_queryset(self):
        return Listing.objects.filter(user=self.request.user)


class CreateListingView(LoginRequiredMixin, View):
    login_url = '/login/'
    form_class = ListingForm
    template_name = 'create_listing.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_listing = form.save(commit=False)

            new_listing.user = request.user
            new_listing.is_active = True
            new_listing.save()
            
            return HttpResponseRedirect('/listings/')

        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class DeleteListingView(LoginRequiredMixin, View):
    login_url = '/login/'
    template_name = 'delete_listing.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, pk, *args, **kwargs):
        listing = Listing.objects.get(pk=pk)
        if request.user == listing.user:
            listing.delete()
            return HttpResponseRedirect('/listings/')
        else:
            return HttpResponse(403)
