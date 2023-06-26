from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    email_address = models.EmailField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Client {self.first_name} {self.middle_name} {self.last_name}'
