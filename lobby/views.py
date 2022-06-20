from django.shortcuts import render
from .models import Message ,Thread

# Create your views here.


def room(request):
    thread = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {
        'thread' : thread,
    }
    print(thread)
    return render(request, 'lobby/room.html',context)
