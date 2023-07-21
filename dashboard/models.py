from django.db import models
from django.contrib.auth.models import User
import uuid
from django.urls import reverse
from datetime import datetime

# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    # our_ref = models.UUIDField(max_length=20, default= uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=12)
    email_address = models.EmailField()
    address = models.CharField(max_length=50, blank=True, null=True)
    address_line_2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)
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
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'Client {self.first_name} {self.last_name}'


class ClientNote(models.Model):
    title = models.CharField(max_length=200, unique=True)
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='notes', blank=True, null=True)
    employee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f'Client note {self.title}'


class ToDoList(models.Model):
    task = models.CharField(max_length=60, unique=False)
    complete = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f'To-do-list'


# Appointment booking form

TIME_PERIODS = (
    ("10 AM", "10AM"),
    ("11 AM", "11 AM"),
    ("12 PM", "12PM"),
    ("2 PM", "2 PM"),
    ("3 PM", "3PM"),
    ("4 PM", "4 PM"),
    ("5 PM", "5 PM"),
)

class Appointment(models.Model):
    first_name = first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_a_client = models.BooleanField(default=False)
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='appointments', blank=True, null=True)
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=5, choices=TIME_PERIODS, default="")
    phone_number = models.CharField(max_length=12)
    email_address = models.EmailField(blank=True, null=True)
    app_note = models.TextField()

    def __str__(self):
        return f'Appointments {self.title}'
