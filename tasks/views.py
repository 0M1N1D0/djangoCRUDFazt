from django.shortcuts import render, redirect
from .models import Tareas


# Create your views here.
def list_tasks(requests):
    tareas = Tareas.objects.all()
    return render(requests, 'tasks/list_tasks.html', {'tasks':tareas})


def create_task(request):
    # print(request.POST)
    task = Tareas(title=request.POST['title'], description=request.POST['description'])
    task.save()
    return redirect('/tasks/')


def delete_task(request, task_id):
    task = Tareas.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks/')
