from django.shortcuts import render, redirect
from .models import Disaster
from .form import DisasterForm
from django.contrib.auth.decorators import login_required

@login_required
def disaster_list(request):
    # Logic for displaying disasters
    pass

@login_required
def disaster_create(request):
    # Logic for creating a disaster
    pass

def disaster_list(request):
    disasters = Disaster.objects.all()
    return render(request, 'disaster_list.html', {'disasters': disasters})

def disaster_create(request):
    if request.method == 'POST':
        form = DisasterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disaster_list')
    else:
        form = DisasterForm()
    return render(request, 'disaster_form.html', {'form': form})

def disaster_update(request, pk):
    disaster = Disaster.objects.get(pk=pk)
    if request.method == 'POST':
        form = DisasterForm(request.POST, instance=disaster)
        if form.is_valid():
            form.save()
            return redirect('disaster_list')
    else:
        form = DisasterForm(instance=disaster)
    return render(request, 'disaster_form.html', {'form': form})

def disaster_delete(request, pk):
    disaster = Disaster.objects.get(pk=pk)
    disaster.delete()
    return redirect('disaster_list')
