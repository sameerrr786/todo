from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    task=request.POST['task'] # Debugging line to check POST data 
    Task.objects.create(task=task)
    return redirect('home')  # Placeholder response for task addition

def mark_as_done(request,pk):
    task=get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')  # Redirect to home after marking task as done