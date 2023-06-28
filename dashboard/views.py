from django.shortcuts import render, redirect
from .forms import ClientForm, CallLogForm
from .models import Client
from django.views.generic.edit import CreateView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

# homepage index


def index(request):
    return render(request, 'index.html')

# New client form

# def create_client(request):
#     if request.method == 'POST':
#         form = ClientForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'New clients created')
#             return redirect('index')
#     else:
#         form = ClientForm()

#     return render(request, 'new_client.html', {'form': form})


class CreateClient(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'new-client.html'
    success_url = reverse_lazy('index')


# call log
def phone_log(request):
    if request.method == 'POST':
        form = CallLogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Call logged')
            return redirect('index')
    else:
        form = CallLogForm()

    return render(request, 'call-log-form.html', {'form': form, })
