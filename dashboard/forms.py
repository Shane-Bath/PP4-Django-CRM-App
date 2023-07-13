from django import forms
from .models import Client, PhoneLog, ClientNote, ToDoList
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# from allauth.account.forms import SignupForm


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('first_name', 'middle_name', 'last_name',
                  'phone_number', 'email_address', 'address', 'address_line_2', 'city', 'county', 'eircode')


# Cripy versions

#  Logging calls

# class CallLogForm(forms.Form):
#     first_name = forms.CharField(label='First Name')
#     last_name = forms.CharField(label='last Name')
#     phone_number = forms.IntegerField(label='Phone Number')
#     message = forms.Textareatext = forms.CharField(
#         widget=forms.Textarea(attrs={"rows": 7, "cols": 40}),
#         label="Message",
#     )

class CallLogForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CallLogForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'Save'))

    class Meta:
        model = PhoneLog
        fields = ('first_name', 'last_name', 'phone_number', 'message')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
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
