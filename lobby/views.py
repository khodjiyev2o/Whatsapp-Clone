from django.shortcuts import render
from .models import Message ,Thread

# Create your views here.


def room(request):
    thread = Thread.objects.by_user(user=request.user).prefetch_related('message_thread').order_by('timestamp')
    for th in thread :
        messages = Message.objects.filter(thread__id=th.id)
    context = {
        'thread' : thread,
        'messages' : messages
    }
    print(thread)
    return render(request, 'lobby/room.html',context)
