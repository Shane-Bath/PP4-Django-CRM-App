from django import forms
from .models import Client, PhoneLog, ClientNote, ToDoList
# from allauth.account.forms import SignupForm


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('first_name', 'middle_name', 'last_name',
                  'phone_number', 'email_address', 'address', 'address_line_2', 'city', 'county', 'eircode')


class CallLogForm(forms.ModelForm):
    class Meta:
        model = PhoneLog
        fields = ('first_name', 'last_name', 'phone_number', 'message')


class ClientNoteForm(forms.ModelForm):
    class Meta:
        model = ClientNote
        fields = ('title', 'employee', 'content')


class TaskForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ('task',)


