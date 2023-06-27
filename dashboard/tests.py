from django.test import TestCase
from .models import Client, PhoneLog

# Create your tests here.


def test_client(self):
    client = Client.objects.get(id=1)
    self.assertEqual(client.first_name, 'Shane')
    self.assertEqual(client.email_address, 'Shane')


def test_phone_log(self):
    self.assertEqual(PhoneLog.first_name, ' ')
