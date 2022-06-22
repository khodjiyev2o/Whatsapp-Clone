from django.test import TestCase
from .models import Message,Thread
from django.contrib.auth.models import User
# Create your tests here.




class MessageTestCase(TestCase):

    def setUp(self):

        user = User.objects.create(username="Samandar",email="samandar@gmail.com",password="sam12345")
        user1 = User.objects.create(username="Anvarov", email="samandar@gmail.com", password="sam12345")
        thread = Thread.objects.create(first_person=user,second_person=user1,)

        Message.objects.create(context="hello",owner=user,thread=thread)


    def test_thread_counter(self):
        thread = Thread.objects.count()
        self.assertEqual(thread, 1)

    def test_message_counter(self):
        message = Message.objects.count()
        self.assertEqual(message,1)

    def test_message_context(self):
        user1 = User.objects.get(username="Samandar")
        prohibited_words = ['mother','father']
        message = Message.objects.get(owner=user1)
        for word in prohibited_words:
            self.assertNotEqual(message.context, word)