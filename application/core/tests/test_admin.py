from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class TestUserAdmin(TestCase):

    def setUp(self):
        self.client = Client()
        User = get_user_model()
        self.admin_user = User.objects.create_superuser(
            email="anubhav@google.com",
            password="abcd123"
        )
        
        self.client.force_login(self.admin_user) 
        self.user = User.objects.create_user(
            email="anubhav@gmail.com",
            password="abcd123"
        )
        

    def test_user_listing(self):
        url = reverse("admin:core_user_changelist")
        print("admin url: ".format(url))
        response = self.client.get(url)
        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)