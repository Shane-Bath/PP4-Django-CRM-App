from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClientForm, CallLogForm, ClientNoteForm, TaskForm
from .models import Client, PhoneLog, ClientNote, ToDoList
from django.views.generic import CreateView, View, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormView
from django.views import generic, View
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.core.paginator import Paginator

# Create your views here.

# homepage index


def index(request):

    return render(request, 'index.html')


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


# New Client

@method_decorator(login_required, name='dispatch')
class CreateClient(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'new-client.html'
    success_url = reverse_lazy('dashboard')


# call log
@method_decorator(login_required, name='dispatch')
class CallLog(View):
    def get(self, request):
        form = CallLogForm()
        return render(request, 'call-log-form.html', {'form': form})

    def post(self, request):
        form = CallLogForm(request.POST)
        if form.is_valid():
            # first_name = form.cleaned_data.get('first_name')
            # client = get_object_or_404(Client, first_name=first_name)
            call_log = form.save(commit=False)
            # call_log.Client = Client
            call_log.save()
            messages.success(self.request, 'Call logged')
            return redirect('dashboard')
            # return JsonResponse({'message': 'Call logged'})
        else:
            # return JsonResponse({'error': form.errors}, status=400)
            return render(request, 'call-log-form.html', {'form': form, })


# call log modal

# Delete calls
class DeleteCall(DeleteView):
    model = PhoneLog
    fields = ["pk"]
    template_name = 'delete-call.html'
    success_url = reverse_lazy('dashboard')

# Delete call from html list but not database- soft delete I will continue to
# work on this

# class DeleteCall(DeleteView):
#     model = PhoneLog
#     template_name = 'delete-call.html'

#     def delete(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         self.object.is_deleted = True
#         self.object.save()

#         return redirect('dashboard')

    # fields = ["pk"]
    # template_name = 'delete-call.html'
    # success_url = reverse_lazy('dashboard')

# def delete_call(request, pk):
#     call = get_object_or_404(PhoneLog, pk=pk)
#     call.is_deleted = True
#     call.save()
#     return redirect('dashboard')

# Display call log


# @login_required
# def display_call_log(request):
#     call_logs = PhoneLog.objects.all().order_by('-created_on')
#     paginate_by = 3

#     context = {
#         'call_logs': call_logs,

#     }

#     return render(request, 'display-call.html', context)

# Call log now with pagination!


class DisplayCallLog(ListView):
    model = PhoneLog
    form_class = CallLogForm
    template_name = 'display-call.html'
    paginate_by = 4
    success_url = reverse_lazy('dashboard')
    context_object_name = 'call_logs'
    extra_context = {'is_paginated': True}


class DashCallLog(ListView):
    model = PhoneLog
    form_class = CallLogForm
    template_name = 'dashboard.html'
    paginate_by = 4
    context_object_name = 'call_logs'
    extra_context = {'is_paginated': True}

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     paginator = context['paginator']
    #     page = context['page_obj']
    #     context['is_paginated'] = paginator.num_pages > 1
    #     return context


# display all clients


@ login_required
def display_clients(request):
    clients_list = Client.objects.all()

    return render(request, 'client-list.html', {'clients_list': clients_list})


@ login_required
def client_list(request):
    dash_client = get_object_or_404(Client)
    return render(request, 'dash-client-list.html', {'dash_client': dash_client})

# Individual client


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


# Edit client details


def update_client(request, id):
    edit_client = get_object_or_404(Client, id=id)
    edit_form = ClientForm(request.POST or None, instance=edit_client)

    if request.method == 'POST':
        if edit_form.is_valid():
            edit_form.save()
            return redirect('details', id=id)

    return render(request, 'edit-client.html', {'edit_form': edit_form, 'edit_client': edit_client})
# Search Clients


@ login_required
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

    context = {
        'client': client,
        'notes': notes,
        'form': form,
    }

    return render(request, 'edit-note.html', context)

# render the note assoicated with the client


@ login_required
def display_client_note(request, id):
    client = get_object_or_404(Client, id=id)
    notes_display = ClientNote.objects.filter(client_id=id)
    paginator = Paginator(notes_display, 5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'client': client,
        'notes_display': notes_display,
        'page_obj': page_obj,
        'page_number': int(page_number),
    }

    return render(request, 'note.html', context)

#  Delete note


class DeleteNote(DeleteView):
    model = ClientNote
    fields = ['title', 'employee', 'content']
    template_name = 'delete-task.html'
    success_url = reverse_lazy('details')


# To do list

# @method_decorator(login_required, name='dispatch')
class TaskList(CreateView):
    model = ToDoList
    form_class = TaskForm
    template_name = 'task-list.html'
    success_url = reverse_lazy('')


# Display to do list


def display_task(request):
    tasks = ToDoList.objects.all().order_by('-created_on')
    # breakpoint()

    return render(request, 'task.html', {'tasks': tasks})

# Task Update


class UpdateTask(UpdateView):
    model = ToDoList
    fields = ["task"]
    template_name = 'task-update.html'
    success_url = reverse_lazy('dashboard')


# task delete


class DeleteTask(DeleteView):
    model = ToDoList
    fields = ["task"]
    template_name = 'delete-task.html'
    success_url = reverse_lazy('dashboard')


# Custom login

# class CustomLogin(Loginform):
#     def login(self, *args, **kwargs):
