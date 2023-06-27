from django.contrib import admin
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm
from .models import Client, PhoneLog

admin.site.register(Client)
admin.site.register(PhoneLog)
