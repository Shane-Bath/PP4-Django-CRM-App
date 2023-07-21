from django.contrib import admin
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm, LoginForm
from .models import Client, PhoneLog, ClientNote, ToDoList, Appointment

admin.site.register(Client)
admin.site.register(PhoneLog)
admin.site.register(ClientNote)
admin.site.register(ToDoList)
admin.site.register(Appointment)
