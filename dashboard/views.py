from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClientForm, CallLogForm, ClientNoteForm, TaskForm, EditClientForm, EditClientNoteForm
from .models import Client, PhoneLog, ClientNote, ToDoList, Appointment
from django.views.generic import CreateView, View, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormView
from django.views import generic, View
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.mixins import UserPassesTestMixin


# homepage index

'''
Main landing page with login and signup links
'''


def index(request):

    return render(request, 'index.html')

# Dashboard


'''
The Dashbord the user can navigate to different apps. Center page of the project
'''


@login_required
def dashboard(request):
    clients_list = Client.objects.all()
    call_logs = PhoneLog.objects.all().order_by('-created_on')
    tasks = ToDoList.objects.all().order_by('-created_on')
    task_update = UpdateTask()
    delete_task = DeleteTask()
    call_delete = DeleteCall()

    context = {
        'clients_list': clients_list,
        'call_logs': call_logs,
        'tasks': tasks,
        'task_update': task_update,
        'delete_task': delete_task,
        'call_delete': call_delete,
    }
    return render(request, 'dashboard.html', context)


# Clients
'''
Create a new Client form
'''


@method_decorator(login_required, name='dispatch')
class CreateClient(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'new-client.html'
    success_url = reverse_lazy('dashboard')


'''
Create a client folder with with client details and associated note
'''


@ login_required
def clients_file(request, id):
    details = get_object_or_404(Client,
                                id=id,)
    form = ClientNoteForm(request.POST)
    client = get_object_or_404(Client, id=id)
    notes = ClientNote.objects.filter(
        client=client).order_by('-created_on')[:5]
    notes_display = ClientNote.objects.filter(client=client)
    edit_client = get_object_or_404(Client, id=id,)
    edit_form = ClientForm(request.POST or None)

    context = {
        'details': details,
        'notes': notes,
        'client': client,
        'form': form,
        'notes_display': notes_display,
        'edit_client': edit_client,
        'edit_form': edit_form,
        'form': form,
    }

    return render(request, 'clients-folder.html',  context)


# display all clients
'''
Display all clients in the client model and paginate the page
by 10
'''


@ login_required
def display_clients(request):
    clients_list = Client.objects.all().order_by('last_name')
    paginator = Paginator(clients_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    entries = page_obj.object_list

    context = {
        'page_obj': page_obj,
        'entries': entries,
    }

    return render(request, 'client-list.html', context)


# Edit client details
'''
Update Client details using updateview and crispy forms 
'''


class EditClientDetails(UpdateView):
    model = Client
    form_class = EditClientForm
    template_name = 'edit-client.html'
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('details', kwargs={'id': self.object.id})


# Search Clients
'''
Search client data base, with the Q Objects, by name, phone number, email and
address.
'''


@ login_required
def client_search(request):
    query = request.GET.get('query')

    if query:
        clients = Client.objects.filter(
            Q(first_name__icontains=query) |
            Q(middle_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(phone_number__icontains=query) |
            Q(email_address__icontains=query) |
            Q(address__icontains=query)
        )
    else:
        clients = Client.objects.none()

    return render(request, 'client-search-results.html', {'clients': clients})


# Client note
# @method_decorator(login_required, name='dispatch')
'''
Create note and add to the clients folder. limit the number of notes displayed on the
clientfile to 5. 
'''


def display_note(request, id):
    client = get_object_or_404(Client, id=id)
    notes = ClientNote.objects.filter(
        client=client).order_by('-created_on')[:5]
    form = None

    if request.method == 'POST':
        form = ClientNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.client = client
            note.save()
            form = ClientNoteForm()
            return redirect('details', id=id)
    else:
        form = ClientNoteForm()

    context = {
        'client': client,
        'notes': notes,
        'form': form,
    }

    return render(request, 'create-note.html', context)


# render the note assoicated with the client
'''
Show all the note associatd with the client, as the clientfolder itself is limited to 5. 
This page will be paginated to 5. 
'''


@ login_required
def display_client_note(request, id):
    client = get_object_or_404(Client, id=id)
    notes_display = ClientNote.objects.filter(client_id=id)
    paginator = Paginator(notes_display, 5)
    page_number = request.GET.get('page',)
    page_obj = paginator.get_page(page_number)

    context = {
        'client': client,
        'notes_display': notes_display,
        'page_obj': page_obj,
        'page_number': page_number,
    }

    return render(request, 'note.html', context)


#  Delete note
'''
Delete note all users can delete a note. Not restricted. 
'''


class DeleteNote(DeleteView):
    model = ClientNote
    template_name = 'delete-note.html'

    def get_success_url(self):
        return reverse_lazy('note', kwargs={'id': self.object.client.id})


# Edit Note
class EditNote(UpdateView):
    model = ClientNote
    form_class = EditClientNoteForm
    template_name = 'edit-note.html'
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('note', kwargs={'id': self.object.client.id})


# call log
'''
To record phone calls.
'''


@method_decorator(login_required, name='dispatch')
class CallLog(View):
    def get(self, request):
        form = CallLogForm()
        return render(request, 'call-log-form.html', {'form': form})

    def post(self, request):
        form = CallLogForm(request.POST)
        if form.is_valid():
            call_log = form.save(commit=False)
            call_log.save()
            messages.success(self.request, 'Call logged')
            return redirect('dashboard')
        else:
            return render(request, 'call-log-form.html', {'form': form, })


# call log modal

# Delete calls

'''
Delete calls from the call log
'''


class DeleteCall(DeleteView):
    model = PhoneLog
    template_name = 'delete-call.html'
    success_url = reverse_lazy('dashboard')


'''
Display a list of the phone calls with pagination
'''


class DisplayCallLog(ListView):
    model = PhoneLog
    form_class = CallLogForm
    template_name = 'display-call.html'
    paginate_by = 10
    success_url = reverse_lazy('dashboard')
    context_object_name = 'call_logs'
    extra_context = {'is_paginated': True}
    ordering = ['-created_on']


# To do list

# @method_decorator(login_required, name='dispatch')
class TaskList(CreateView):
    model = ToDoList
    form_class = TaskForm
    template_name = 'task-list.html'
    success_url = reverse_lazy('task')


# Display to do list


def display_task(request):
    tasks = ToDoList.objects.all().order_by('-created_on')
    paginator = Paginator(tasks, 5)
    page_number = request.GET.get('page',)
    page_obj = paginator.get_page(page_number)

    return render(request, 'task.html', {'page_obj': page_obj})

# Task Update


class UpdateTask(UpdateView):
    model = ToDoList
    fields = ["task"]
    template_name = 'task-update.html'
    success_url = reverse_lazy('task')


# task delete


class DeleteTask(UserPassesTestMixin, DeleteView):
    model = ToDoList
    fields = ["task"]
    template_name = 'delete-task.html'
    success_url = reverse_lazy('task')

    def test_func(self):
        return self.request.user.is_superuser
