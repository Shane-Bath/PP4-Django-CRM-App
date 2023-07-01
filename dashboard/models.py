from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    # our_ref = models.UUIDField(max_length=20, default= uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=12)
    email_address = models.EmailField()
    address = models.TextField(max_length=500, blank=True, null=True)
    eircode = models.CharField(max_length=7, blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Client {self.first_name} {self.middle_name} {self.last_name}'


class PhoneLog(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    email_address = models.EmailField(blank=True, null=True)
    message = models.TextField(max_length=300)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Client {self.first_name} {self.last_name}'
