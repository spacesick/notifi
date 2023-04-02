from django.urls import path

from .views import UserDetailByIdView, UserListView

urlpatterns = [
    path('by-id/<int:pk>/', UserDetailByIdView.as_view(), name='user-detail'),
    path('', UserListView.as_view(), name='user-list'),
]
