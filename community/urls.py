from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.CommunityListAPIView.as_view(), name="community_list"),
    path("<int:pk>/", views.CommunityDetailAPIView.as_view(), name="community_detail"),
    path("<int:pk>/like/", views.CommunityLikeAPIView.as_view(), name="community_like"),
    path(
        "like_list/",
        views.CommunityLikeListAPIView.as_view(),
        name="community_like_list",
    ),
    path("<int:pk>/comment/", views.CommentListAPIView.as_view(), name="comment_list"),
    path(
        "comment/<int:pk>/", views.CommentEditAPIView.as_view(), name="comment_detail"
    ),
    path(
        "comment/like_list/",
        views.CommentLikeListAPIView.as_view(),
        name="comment_like_list",
    ),
    path(
        "comment/<int:pk>/like/",
        views.CommentLikeAPIView.as_view(),
        name="comment_like",
    ),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
