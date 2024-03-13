from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def indexPage(request):
    all_tasks = Task.objects.all().order_by('priority', 'due_date')
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