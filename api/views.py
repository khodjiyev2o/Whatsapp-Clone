from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .models import Thread, Message
from .serializers import UserSerializer,MessageSerializer,ThreadSerializer

# Create your views here.

@api_view(['GET'])
def usersapi(request):
    queryest = User.objects.all()
    serializer = UserSerializer(queryest,many=True)
    return Response(serializer.data)



@api_view(['GET'])
def messagesapi(request):
    queryest = Message.objects.all()
    serializer = MessageSerializer(queryest,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def threadsapi(request):
    queryest = Thread.objects.all()
    serializer = ThreadSerializer(queryest,many=True)
    return Response(serializer.data)
