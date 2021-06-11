from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Task
from .forms import TaskForm
from django.urls import reverse
# Create your views here.

def index(request):
    tasks = Task.objects.all().order_by('-date_created')
    form = TaskForm
    if request.method == "POST" and request.POST['submit'] == "Add":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todo:index'))
    return render(request, 'todo/index.html', {
        'tasks':tasks,
        'form':form
    })

def update(request, q_id):
    task = get_object_or_404(Task, pk=q_id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todo:index'))
    return render(request, 'todo/update.html', {
        'task':task,
        'form':form
    })


def delete(request, q_id):
    task = get_object_or_404(Task, pk=q_id)
    if request.method == "POST":
        task.delete()
        return HttpResponseRedirect(reverse('todo:index'))
    return render(request, 'todo/delete.html', {
        'task':task
    })