from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path("",views.UserCreateView.as_view()),
    path("signin/",views.UserSigninView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("<str:username>/", views.UserProfileView.as_view()),
    path("signout/", views.UserSignoutView.as_view()),
    path("password_update/", views.UserPasswordUpdateView.as_view()), 
]
