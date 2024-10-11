from django.urls import path
from .views import SummaryAPIView


urlpatterns = [
    
    path("summary/<int:evaluation_id>/", SummaryAPIView.as_view(), name="summary"),

]