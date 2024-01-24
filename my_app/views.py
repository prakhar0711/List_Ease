from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def home(request):
    """
    Renders the 'home.html' template with the tasks and form as context variables.
    Accepts a request object as a parameter. No return value.
    """
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    # Display the contents by creating a dictionary
    context = {'tasks': tasks, 'form': form}
    return render(request, 'my_app/home.html', context)


def update_task(request, pk):
    """
    Renders the 'update_task.html' template with the task and form as context variables.
    Accepts a request object as a parameter. No return value.
    """
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'my_app/update_task.html', context)

def delete(request, pk):
    """
    Accepts a request object as a parameter. No return value.
    """
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'my_app/delete.html', context)
