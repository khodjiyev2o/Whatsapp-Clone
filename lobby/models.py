from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Thread(models.Model):
    first_person = models.ForeignKey(User,on_delete = models.CASCADE,related_name='first_person')
    second_person = models.ForeignKey(User,on_delete = models.CASCADE,related_name='second_person')


class Message(models.Model):
    context = models.CharField(max_length=150)
    owner = models.ForeignKey(User,on_delete = models.CASCADE)
    thread = models.ForeignKey(Thread,on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.context)

    class Meta:
        ordering = ('date',)