from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClientForm, CallLogForm, ClientNoteForm
from .models import Client, PhoneLog, ClientNote
from django.views.generic import CreateView, View
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

# homepage index


def index(request):
    return render(request, 'index.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


# New Client

@method_decorator(login_required, name='dispatch')
class CreateClient(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'new-client.html'
    success_url = reverse_lazy('dashboard')


# call log
@method_decorator(login_required, name='dispatch')
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

# Display clients


# class DisplayClients(CreateView):
#     model = Client
#     queryset = Client.objects.all()
#     template_name = 'client-list.html'
#     paginate_by = 10

@login_required
def display_clients(request):
    clients_list = Client.objects.all()

    return render(request, 'client-list.html', {'clients_list': clients_list})


@login_required
def client_list(request):
    dash_client = Client.objects.all()
    return render(request, 'dashboard.html', {'dash_client': dash_client})
# Individual client


@login_required
def clients_file(request, id):
    details = get_object_or_404(Client,
                                id=id,)

    return render(request, 'clients-folder.html', {'details': details})

# Search Clients


@login_required
def client_search(request):
    query = request.GET.get('query')

    if query:
        clients = Client.objects.filter(
            Q(first_name__icontains=query) |
            Q(middle_name__icontains=query) |
            Q(last_name__icontains=query)
        )
    else:
        clients = Client.objects.none()

    return render(request, 'client-search-results.html', {'clients': clients})

# Client note


# @method_decorator(login_required, name='dispatch')
# class DisplayNote(View):

# def display_note(request, Client):
#     client = get_object_or_404(Client, id=id)
#     notes = client.clientnote_set.all()

#     return render(request, 'clients-folder.html', {'client': client, 'notes': notes})

# def client_detail(request, client_id):
#     client = get_object_or_404(Client, id=id)
#     notes = client.notes.all()
#     form = ClientNoteForm()

#     if request.method == 'POST':
#         form = ClientNoteForm(request.POST)
#         if form.is_valid():
#             note = form.save(commit=False)
#             note.client = client
#             note.save()
#             form = ClientNoteForm()

#     context = {
#         'client': client,
#         'notes': notes,
#         'form': form,
#     }
#     return render(request, 'clients-folder.html', context)
