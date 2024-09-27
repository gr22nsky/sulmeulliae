from django.urls import path
from . import views

urlpatterns = [
    path("", views.CommunityListAPIView.as_view(), name="community_list"),
    path("<int:pk>/", views.CommunityDetailAPIView.as_view(), name="community_detail"),
    path("<int:pk>/like/", views.CommunityLikeAPIView.as_view(), name="community_like"),
    path("comment/", views.CommentListPIView.as_view(), name="comment_list"),
    path("comment/<int:pk>/", views.CommentEditAPIView.as_view(), name="comment_detail"),
    path("comment/<int:pk>/like/", views.CommentLikeAPIView.as_view(), name="comment_like"),
]
