from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.

class TodoTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="adnan", password="20021232")
        User.objects.create(username="adnan1", password="20021232")

    def test_todo_user(self):
        user = User.objects.get(username="adnan")

        self.assertEqual(user.username, "adnan")
        self.assertEqual(user.password, "20021232")

    def test_set_information(self):
        user = User.objects.get(username="adnan")

        user.first_name = "Adnan"
        user.last_name = "Kamali"

        user.save()
        user = User.objects.get(username="adnan")
        
        self.assertEqual(user.first_name, "Adnan")
