import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Room,Message
from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name,


        )

        await self.accept()






    async def receive(self,text_data):
        text_data = json.loads(text_data)
        message = text_data['message']
        user = text_data['user']

        room = text_data['room']
        message = Message.objects.create(context=message, owner=self.scope['user'], room=self.room_name)
        await  self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_message',
                'message': message,
                'user' : user
            }
        )

    async def user_message(self, event):
        message = event['message']
        user = event['user']
        await self.send(json.dumps({
            'message': message,
            'user': user
        })
         )




    async def disconnect(self,close_code):

        # Join room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

