from django.urls import path

from .views import UserLoginView, UserLogoutView, UserRegisterView

from django.views.generic.base import RedirectView

urlpatterns = [
    # path('by-id/<int:pk>/', UserDetailByIdView.as_view(), name='user-detail'),
    # path('', UserListView.as_view(), name='user-list'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('', RedirectView.as_view(url='/listings/', permanent=False), name='index')
]
