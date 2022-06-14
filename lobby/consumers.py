import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name,
                print(self.channel_name)

        )

    async def disconnect(self,close_code):

        # Join room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
