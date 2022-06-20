from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models import Q, UniqueConstraint
from django.db.models.functions import Lower


class ThreadManager(models.Manager):
    def by_user(self, **kwargs):
        user = kwargs.get('user')
        lookup = Q(first_person=user) | Q(second_person=user)
        qs = self.get_queryset().filter(lookup).distinct()
        return qs



class Thread(models.Model):
    first_person = models.ForeignKey(User,on_delete = models.CASCADE,related_name='first_person')
    second_person = models.ForeignKey(User,on_delete = models.CASCADE,related_name='second_person')
    objects  = ThreadManager()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:

        unique_together = (
            ('first_person', 'second_person'),
            ('second_person', 'first_person'),
        )


class Message(models.Model):
    context = models.CharField(max_length=150)
    owner = models.ForeignKey(User,on_delete = models.CASCADE)
    thread = models.ForeignKey(Thread,on_delete = models.CASCADE,blank=True, null=True,related_name='message_thread')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.context)

    class Meta:
        ordering = ('date',)