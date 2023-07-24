from django.contrib.auth.models import User
from django.test import TestCase, Client
from .models import Client, PhoneLog
from django.urls import reverse
import unittest
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.staticfiles import finders
# Create your tests here.


class MyTest(unittest.TestCase):
    self.assertTrue(staticfiles_storage.exists(finders.find(static/css/style.css')))