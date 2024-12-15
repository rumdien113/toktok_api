from django.urls import path
from .views import RegisterView, UserListCreateView, UserDetailView, LoginView, LogoutView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('users', UserListCreateView.as_view()),
    path('users/<uuid:id>', UserDetailView.as_view()),
]
