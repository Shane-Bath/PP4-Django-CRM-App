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
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'phone Number'}),
            'message': forms.Textarea(attrs={'placeholder': 'Message'}),
        }


class ClientNoteForm(forms.ModelForm):
    class Meta:
        model = ClientNote
        fields = ('title', 'employee', 'content')


class TaskForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ('task',)
