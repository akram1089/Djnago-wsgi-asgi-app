# routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/some_path/", consumers.YourWebSocketConsumer.as_asgi()),
    # Add more WebSocket paths and consumers as needed
]

application = ProtocolTypeRouter({
    "websocket": URLRouter(
        websocket_urlpatterns
    ),
})
