from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.EvaluationListView.as_view(), name='evaluation_list'),
    path('<int:pk>/', views.EvaluationDetailView.as_view(), name='evaluation_detail'),
    path('<int:pk>/review/', views.ReviewListView.as_view(), name='review'),
    path('review/<int:pk>/', views.ReviewDetailView.as_view(), name='review_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
