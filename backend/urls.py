from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("admin/", admin.site.urls),
    path("",include("allauth.urls")),
    path("api/v1/accounts/", include("accounts.urls")),
    path("api/v1/evaluations/", include("evaluations.urls")),
    path("api/v1/community/", include("community.urls")),
    path("api/v1/chatbot/", include("chatbot.urls")),
    path('api/v1/chat/', include('chat.urls')),
    path("api/v1/products/", include("products.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)), ]
