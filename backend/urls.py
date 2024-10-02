from django.contrib import admin
from django.urls import path, include
from . import settings


urlpatterns = [
    
    path('admin/',admin.site.urls),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v2/accounts/', include('accounts.urls')),
    path('api/v1/evaluations/', include('evaluations.urls')),
    path('api/v1/community/', include('community.urls')),
    
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)), ]
