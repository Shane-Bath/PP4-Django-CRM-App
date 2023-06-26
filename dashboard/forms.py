from django import forms
from .models import Client
# from allauth.account.forms import SignupForm


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
