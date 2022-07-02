from django.contrib import admin
from .models import User, Message, Thread


# Register your models here.


class ChatMessage(admin.TabularInline):
    model = Message


class ThreadAdmin(admin.ModelAdmin):
    inlines = [ChatMessage]

    class Meta:
        model = Thread


admin.site.register(Thread, ThreadAdmin)
admin.site.register(Message)
