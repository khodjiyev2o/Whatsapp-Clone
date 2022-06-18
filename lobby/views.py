from django.shortcuts import render
from .models import Room,Message

# Create your views here.


def room(request):
    return render(request, 'lobby/room.html', {

    })
