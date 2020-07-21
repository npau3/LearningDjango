from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.http import HttpResponseRedirect


def index(request):
    tasks = Task.objects.all().order_by('id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    success = False
    error = ''
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            success = True
            form.save()
            return redirect('create')
        else:
            error = 'Форма была неверной'
    form = TaskForm()
    context = {
        'form': form,
        'error': error,
        'success': success
    }
    return render(request, 'main/create.html', context)


def update_page(request):
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)