from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Room(models.Model):
    roomname = models.CharField(max_length=15,blank=False)
    members = models.ManyToManyField(User,blank=False)

    def __str__(self):
        return str(self.roomname)

class Message(models.Model):
    context = models.CharField(max_length=150)
    owner = models.ForeignKey(User,on_delete = models.CASCADE)
    room = models.ForeignKey(Room,on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.context)