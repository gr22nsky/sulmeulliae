from django.urls import path
from . import views

urlpatterns = [
    path('', views.EvaluationsListView.as_view(), name='evaluation_list'),
    path('<int:pk>/', views.EvaluationDetailView.as_view(), name='evaluation_detail'),
]
