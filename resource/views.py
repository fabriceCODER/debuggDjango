from django.shortcuts import render, redirect
from .models import Resource
from .form import ResourceForm
from django.contrib.auth.decorators import login_required

@login_required
def resource_list(request):
    resources = Resource.objects.all()
    return render(request, 'resource/resource_list.html', {'resources': resources})

@login_required
def resource_create(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resource_list')
    else:
        form = ResourceForm()
    return render(request, 'resource/resource_form.html', {'form': form})


def resource_list(request):
    resources = Resource.objects.all()
    return render(request, 'resource_list.html', {'resources': resources})

def resource_create(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resource_list')
    else:
        form = ResourceForm()
    return render(request, 'resource_form.html', {'form': form})

def resource_update(request, pk):
    resource = Resource.objects.get(pk=pk)
    if request.method == 'POST':
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            form.save()
            return redirect('resource_list')
    else:
        form = ResourceForm(instance=resource)
    return render(request, 'resource_form.html', {'form': form})

def resource_delete(request, pk):
    resource = Resource.objects.get(pk=pk)
    resource.delete()
    return redirect('resource_list')
