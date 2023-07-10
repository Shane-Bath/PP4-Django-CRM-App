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

    # check_client = forms.ModelChoiceField(
    #     queryset=Client.objects.all(),
    #     to_field_name='first_name',
    #     required=True,
    #     widget=forms.Select(attrs={'class': 'form-control'})
    # )


class ClientNoteForm(forms.ModelForm):
    class Meta:
        model = ClientNote
        fields = ('title', 'employee', 'content')


class TaskForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = '__all__'


# class UpdateTaskForm(forms.ModelForm):
#     class Meta:
#         model = ToDoList
#         fields = '__all__'
