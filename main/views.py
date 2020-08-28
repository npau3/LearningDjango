from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, TemplateView, CreateView
from django.db.models import Q


class HomeListView(ListView):
    model = Task
    template_name = 'main/index.html'
    context_object_name = 'tasks'


class AboutListView(TemplateView):
    template_name = 'main/about.html'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'main/create.html'
    form_class = TaskForm
    success_url = reverse_lazy('home')


class UpdateTaskView(UpdateView):
    model = Task
    template_name = 'main/create.html'
    form_class = TaskForm
    success_url = reverse_lazy('home')


# class DeleteTaskView(DeleteView):
#     model = Task
#     template_name = 'main/index.html'
#     success_url = reverse_lazy('home')
#
#     def deletetask(self, pk):
#         tasks = Task.objects.get(id=pk)
#         tasks.delete()
#         return redirect(reverse('home'))


def delete_page(request, pk):
    get_task = Task.objects.get(pk=pk)
    get_task.delete()
    return redirect(reverse('home'))


class SearchResultsView(ListView):
    model = Task
    template_name = 'main/index.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        query = self.request.GET.post('q')
        tasks= Task.objects.filter(
            Q(product__icontains=query) | Q(amount__icontains=query)
        )
        return tasks


# def create(request):
#     success = False
#     error = ''
#     if request.method == "POST":
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             success = True
#             form.save()
#             return redirect('home')
#         else:
#             error = 'Форма была неверной'
#     form = TaskForm()
#     context = {
#         'form': form,
#         'error': error,
#         'success': success
#     }
#     return render(request, 'main/create.html', context)


# def update_page(request, pk):
#     get_task = Task.objects.get(pk=pk)
#     tasks = Task.objects.all().order_by('id')
#     context = {
#         'get_task': get_task,
#         'form': TaskForm(instance = get_task),
#         'tasks': tasks
#     }
#     if request.method == "POST":
#         form = TaskForm(request.POST,instance = get_task)
#         if form.is_valid():
#             form.save()
#         return render(request, 'main/index.html', context)
#     return render(request, 'main/create.html', context)




