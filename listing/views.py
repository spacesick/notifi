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


# class ListingDetailByIdView(generics.RetrieveAPIView):
#     queryset = Listing.objects.all()
#     serializer_class = ListingSerializer
#     permission_classes = [IsAdminUser]


# class ListingListView(generics.ListAPIView):
#     serializer_class = ListingSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Listing.objects.filter(user=self.request.user)
    

# class ListingListAllView(generics.ListAPIView):
#     queryset = Listing.objects.all()
#     serializer_class = ListingSerializer
#     permission_classes = [IsAdminUser]


# class ListingCreate(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'create_listing.html'

#     def get(self, request):
#         serializer = ListingSerializer(profile)
#         return Response({
#             'serializer': serializer, 
#         })

#     def post(self, request):
#         profile = get_object_or_404(Profile, pk=pk)
#         serializer = ProfileSerializer(profile, data=request.data)
#         if not serializer.is_valid():
#             return Response({'serializer': serializer, 'profile': profile})
#         serializer.save()
#         return redirect('profile-list')


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
            
            return HttpResponseRedirect('/')

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
        listing = Listing.object.get(pk=pk)
        if request.user == listing.user:
            listing.delete()
            return HttpResponse(204)
        else:
            return HttpResponse(403)


# class ListingViewSet(viewsets.ModelViewSet):
#     queryset = Listing.objects.all()
#     serializer_class = ListingSerializer

#     def retrieve(self, request, pk=None):
#         queryset = Listing.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = ListingSerializer(user, context={'request': request})
#         return Response(serializer.data)
    
#     @action(detail=False, permission_classes=[IsAuthenticated])
#     def list(self, request):
#         queryset = Listing.objects.filter(user=request.user)
#         serializer = ListingSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)

#     @action(detail=False, permission_classes=[IsAdminUser])
#     def list_all(self, request):
#         queryset = Listing.objects.all()

#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True, context={'request': request})
#             return self.get_paginated_response(serializer.data)

#         serializer = self.get_serializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)