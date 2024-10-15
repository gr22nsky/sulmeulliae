from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.UserAPIView.as_view()),
    path("signin/", views.UserSigninAPIView.as_view()),
    path("signout/", views.UserSignoutAPIView.as_view()),
    path("password_update/", views.UserPasswordUpdateAPIView.as_view()),
    path("token_refresh/", TokenRefreshView.as_view()),
    path("info/", views.UserInfoView.as_view()),
    path("<str:username>/", views.UserProfileAPIView.as_view()),
    path('<str:username>/likes_all/', views.UserLikesAPIView.as_view(), name='user-likes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   