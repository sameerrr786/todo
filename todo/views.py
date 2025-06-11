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

def mark_as_undone(request,pk):
    task=get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')  # Redirect to home after marking task as done

def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:  # Redirect to home after editing task
        context = {'get_task': get_task}
    return render(request, 'edit_task.html', context)  # Render edit task template

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')  # Redirect to home after deleting task