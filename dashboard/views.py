from django.shortcuts import render, redirect
from .forms import ClientForm, CallLogForm
from .models import Client
from django.contrib import messages
# Create your views here.

# homepage index


def index(request):
    return render(request, 'index.html')

# New client form


def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New clients created')
            return redirect('index')
    else:
        form = ClientForm()

    return render(request, 'new_client.html', {'form': form})

# Call log


def phone_log(request):
    if request.method == 'POST':
        form = CallLogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Call logged')
            return redirect('index')
    else:
        form = CallLogForm()

    return render(request, 'call_log_form.html', {'form': form, })
