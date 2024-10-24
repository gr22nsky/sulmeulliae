import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Django의 HTTP 요청을 처리하는 기본 설정
    "websocket": AuthMiddlewareStack(  # WebSocket 요청을 Channels에서 처리
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
