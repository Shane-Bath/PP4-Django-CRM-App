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
    clients_list = Client.objects.all()
    return render(request, 'dashboard.html', {'clients_list': clients_list})


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
def client_list(request,):
    # dash_client = Client.objects.all()
    dash_client = get_object_or_404(Client)
    return render(request, 'dash-client-list.html', {'dash_client': dash_client})

# Individual client


@login_required
def clients_file(request, id):
    details = get_object_or_404(Client,
                                id=id,)
    notes = ClientNote.objects.all()
    form = ClientNoteForm(request.POST)
    client = get_object_or_404(Client, id=id)
    notes_display = ClientNote.objects.filter(client=client)

    context = {
        'details': details,
        'notes': notes,
        'client': client,
        'form': form,
        'notes_display': notes_display,

    }

    return render(request, 'clients-folder.html',  context)

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


def display_note(request, id):
    notes = ClientNote.objects.all()
    client = get_object_or_404(Client, id=id)
    form = None

    if request.method == 'POST':
        form = ClientNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.client = client
            note.save()
            form = ClientNoteForm()
            return redirect('details', id=id)

    context = {
        'client': client,
        'notes': notes,
        'form': form,
    }

    return render(request, 'note-edit.html', context)

# render the note assoicated with the client


@login_required
def display_client_note(request, id):
    client = get_object_or_404(Client, id=id)
    notes_display = ClientNote.objects.filter(client=id)

    return render(request, 'note.html', {'client_id': client, 'notes_display': notes_display})
