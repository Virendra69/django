from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def indexPage(request):
    all_tasks = Task.objects.all().order_by('due_date', 'priority')
    return render(request, 'index.html', {'all_tasks':all_tasks})

def createTask(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        duedate = request.POST.get('duedate')
        priority = request.POST.get('priority')

        task = Task.objects.filter(title=title, description=desc, priority=priority, due_date=duedate).exists()
        if task:
            return redirect('indexPage')
        
        new_task = Task.objects.create(title=title, description=desc, priority=priority, due_date=duedate)
        new_task.save()

        return redirect('indexPage')
    return redirect('indexPage')

def deleteTask(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete_task()
    return redirect('indexPage')