from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    task=request.POST['task'] # Debugging line to check POST data 
    Task.objects.create(task=task)
    return redirect('home')  # Placeholder response for task addition