import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    print('hello world!')