from django.urls import path
from . import views

urlpatterns = [
    path("", views.CommunityListAPIView.as_view(), name="community_list"),
    path("<int:pk>/", views.CommunityDetailAPIView.as_view(), name="community_detail"),
]
