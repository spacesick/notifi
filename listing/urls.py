from django.urls import path

from .views import ListingDetailByIdView, ListingListAllView, ListingListView

urlpatterns = [
    path('by-id/<int:pk>/', ListingDetailByIdView.as_view(), name='listing-detail'),
    path('', ListingListView.as_view(), name='listing-list'),
    path('list-all/', ListingListAllView.as_view(), name='listing-list-all'),
]
