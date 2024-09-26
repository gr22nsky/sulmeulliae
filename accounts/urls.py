from django.urls import path
from . import views

urlpatterns = [
    path("",views.UserCreateView.as_view()),
    path("signin/",views.UserSigninView.as_view()),
    path("<str:username>/", views.UserProfileView.as_view()),
    
    
    
]
