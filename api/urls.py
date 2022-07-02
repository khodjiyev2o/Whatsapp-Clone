
from django.urls import path
from . import views
urlpatterns = [
    path('users/',views.usersapi),
    path('messages/', views.messagesapi),
    path('threads/', views.threadsapi),

]