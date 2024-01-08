from django.urls import path

from channelsdemo.consumers import NumberGenerator

# from .consumers import ZerodhaAPIConsumer


ws_urlpatterns = [
    path(r'ws/', NumberGenerator.as_asgi(), name='number-generator'),
    # path(r"ws/zerodha/", ZerodhaAPIConsumer.as_asgi()),
]
