from django.urls import path
from .views import RegisterView, UserListCreateView, UserDetailView, LoginView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('users', UserListCreateView.as_view()),
    path('users/<uuid:id>', UserDetailView.as_view()),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
