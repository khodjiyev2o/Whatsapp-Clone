from django.test import TestCase
from .models import Message,Thread
from django.contrib.auth.models import User
# Create your tests here.




class MessageTestCase(TestCase):

    def setUp(self):

        user1 = User.objects.create(username="Samandar",email="samandar@gmail.com",password="sam12345")
        user2 = User.objects.create(username="Anvarov", email="samandar@gmail.com", password="sam12345")
        user3 = User.objects.create(username="Abror", email="samandar@gmail.com", password="sam12345")

        #user4 = User.objects.create(username="Kamron", email="samandar@gmail.com", password="sam12345")


        thread1 = Thread.objects.create(first_person=user1,second_person=user2)
        thread2 = Thread.objects.create(first_person=user1, second_person=user3)

        #thread3 = Thread.objects.create(first_person=user1, second_person=user4)
        #thread4 = Thread.objects.create(first_person=user2, second_person=user3)

        Message.objects.create(context="hello",owner=user2,thread=thread1)
        Message.objects.create(context="uzb", owner=user1, thread=thread1)







    def test_thread_counter(self):
        thread = Thread.objects.count()
        self.assertEqual(thread, 2)

    def test_message_counter(self):
        message = Message.objects.count()

        self.assertEqual(message,2)

    def test_message_context(self):
        user1 = User.objects.get(username="Samandar")
        prohibited_words = ['mother','father']
        message = Message.objects.get(owner=user1)
        for word in prohibited_words:
            self.assertNotEqual(message.context, word)

    def test_thread_unique(self):
        samandar= User.objects.get(username="Samandar")
        anvarov = User.objects.get(username="Anvarov")
        thread = Thread.objects.get(first_person=samandar,second_person=anvarov)
        messages = Message.objects.filter(thread=thread)

        def thread_test(messages,user1,user2):
            for message in messages:
                if message.owner != user1 and message.owner != user2:
                    return False
            return True

        self.assertTrue(thread_test(messages,samandar,anvarov))