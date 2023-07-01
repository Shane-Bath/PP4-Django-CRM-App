from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClientForm, CallLogForm
from .models import Client, PhoneLog
from django.views.generic.edit import CreateView, View
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

# homepage index


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'dashboard.html')

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
    success_url = reverse_lazy('dashboard')


# call log
class CallLog(CreateView):
    def get(self, request):
        form = CallLogForm()
        return render(request, 'call-log-form.html', {'form': form, })

    def post(self, request):
        form = CallLogForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            client = get_object_or_404(Client, first_name=first_name)
            call_log = form.save(commit=False)
            call_log.Client = Client
            call_log.save()
            messages.success(request, 'Call logged')
            return redirect('dashboard')
        else:
            return render(request, 'call-log-form.html', {'form': form, })
