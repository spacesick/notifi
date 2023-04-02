from django.urls import path

# from .views import ListingDetailByIdView, ListingListAllView, ListingListView

from .views import CreateListingView, DeleteListingView, ListingsView

urlpatterns = [
    path('<int:pk>/delete/', DeleteListingView.as_view(), name='delete-listing'),
    path('', ListingsView.as_view(), name='listings'),
    path('create/', CreateListingView.as_view(), name='create-listing'),
]
