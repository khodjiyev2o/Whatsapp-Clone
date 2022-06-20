from django.contrib import admin
from .models import Message,Thread
from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q
# Register your models here.


class ChatMessage(admin.TabularInline):
    model = Message



class ThreadAdmin(admin.ModelAdmin):
    inlines = [ChatMessage]

    class Meta:
        model = Thread


admin.site.register(Thread, ThreadAdmin)
admin.site.register(Message)
