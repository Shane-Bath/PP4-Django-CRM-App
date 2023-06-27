from django import forms
from .models import Client
from .models import PhoneLog
# from allauth.account.forms import SignupForm


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class CallLogForm(forms.ModelForm):
    class Meta:
        model = PhoneLog
        fields = '__all__'