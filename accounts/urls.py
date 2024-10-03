from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views


urlpatterns = [
    path("", views.UserAPIView.as_view()),
    path("signin/", views.UserSigninAPIView.as_view()),
    path("signout/", views.UserSignoutAPIView.as_view()),
    path("password_update/", views.UserPasswordUpdateAPIView.as_view()),
    path("token_refresh/", TokenRefreshView.as_view()),
    path("info/", views.UserInfoView.as_view()),
    path("<str:username>/", views.UserProfileAPIView.as_view()),
]
