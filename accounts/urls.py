from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
<<<<<<< HEAD
    path("",views.UserAPIView.as_view()),
    path("signin/",views.UserSigninAPIView.as_view()),
    path("signout/", views.UserSignoutAPIView.as_view()),
    path("password_update/", views.UserPasswordUpdateAPIView.as_view()), 
    path("token/refresh/", TokenRefreshView.as_view()),
    path("<str:username>/", views.UserProfileAPIView.as_view()),
=======
    path("",views.UserCreateView.as_view()),
    path("signin/",views.UserSigninView.as_view()),
    path("signout/", views.UserSignoutView.as_view()),
<<<<<<< HEAD
    path("token/refresh/", TokenRefreshView.as_view()),
    path("<str:username>/", views.UserProfileView.as_view()),
    path("password_update/", views.UserPasswordUpdateView.as_view()), 
>>>>>>> 3349946b31c497bf24034c4268045648063f9a57
]
=======
    path("password_update/", views.UserPasswordUpdateView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("<str:username>/", views.UserProfileView.as_view()),
]
>>>>>>> feature/accounts
