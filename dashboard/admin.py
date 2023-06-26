from django.contrib import admin
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm
from .models import Client

admin.site.register(Client)
