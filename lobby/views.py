from django.shortcuts import render
from .models import Room,Message

# Create your views here.


def index(request):
    return render(request, 'lobby/index.html', {})


def room(request, room_name):
    room_info=Room.objects.get(roomname=room_name)
    messages=Message.objects.filter(room=room_info)
    return render(request, 'lobby/room.html', {
        'room_name': room_name,'messages' : messages
    })
