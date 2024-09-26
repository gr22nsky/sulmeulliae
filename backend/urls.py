from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/evaluations/', include('evaluations.urls')),
    path('api/v1/community/', include('community.urls')),
    
]
