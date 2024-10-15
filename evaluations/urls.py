from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.EvaluationListAPIView.as_view(), name="evaluation_list"),
    path(
        "<int:pk>/", views.EvaluationDetailAPIView.as_view(), name="evaluation_detail"
    ),
    path("<int:pk>/like/", views.EvaluationLikeAPIView.as_view(), name="like"),
    path(
        "liked_evaluations/",
        views.UserLikedEvaluationAPIView.as_view(),
        name="user_liked_evaluations",
    ),
    path("<int:pk>/review/", views.ReviewListAPIView.as_view(), name="review"),
    path("review/<int:pk>/", views.ReviewDetailAPIView.as_view(), name="review_detail"),
    path("review/<int:pk>/like/", views.ReviewLikeAPIView.as_view(), name="like"),
    path(
        "liked_reviews/",
        views.UserLikedReviewAPIView.as_view(),
        name="user_liked_reviews",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)