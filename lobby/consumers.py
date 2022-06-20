import json
from asgiref.sync import async_to_sync, sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message
from django.contrib.auth.models import User

"""
class GroupConsumer(AsyncWebsocketConsumer):
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

        await self.message_save(user,room,message)



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

    @sync_to_async
    def message_save(self,user,room,message):
        room = Room.objects.get(roomname=room)
        username = User.objects.get(username=user)

        Message.objects.create(room=room,owner=username,context=message)
"""


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope['user']
        self.chat_room = f'chat_{user.id}'

        await self.channel_layer.group_add(
            self.chat_room,
            self.channel_name,

        )
        print('connected',self.chat_room)

        await self.accept()






    async def receive(self,text_data):

        text_data = json.loads(text_data)
        message = text_data['message']
        sent_by_id = text_data['sent_by_id']
        sent_to_id = text_data['sent_to_id']
        print(message,'from',sent_by_id,'to',sent_to_id)
        another_user = f'chat_{sent_to_id}'
        response={
            'message': message,
            'sent_by_user': sent_by_id,
            'sent_to_user': sent_to_id,
        }
        await  self.channel_layer.group_send(
            another_user,
            {
                'type': 'chat_message',
                'text': json.dumps(response)
            }
        )

        await  self.channel_layer.group_send(
            self.chat_room,
            {
                'type': 'chat_message',
                'text': json.dumps(response)
            }
        )


    async def chat_message(self, event):
        await self.send(event['text'])
        print('chat_message',event)





    async def disconnect(self,close_code):
        print('disconnected')
        # Join room group
