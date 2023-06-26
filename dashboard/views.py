from django.shortcuts import render
from .forms import ClientForm
# Create your views here.


def index(request):
    return render(request, 'index.html')

def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ClientForm()

    return render(request, 'new_client.html', {'form':form})