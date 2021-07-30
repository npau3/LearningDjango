from .models import Task
from .forms import TaskForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, TemplateView, CreateView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm


class Registration(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'


class HomeListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'main/index.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(author_id=self.request.user.id)


class AboutListView(LoginRequiredMixin, TemplateView):
    template_name = 'main/about.html'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'main/create.html'
    form_class = TaskForm
    success_url = reverse_lazy('home')


class UpdateTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'main/create.html'
    form_class = TaskForm
    success_url = reverse_lazy('home')


class SearchResultsView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'main/index.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        query = self.request.GET.get('q')
        searching = Task.objects.filter(author_id = self.request.user.id)
        tasks = searching.filter(
            Q(product__icontains=query) | Q(amount__icontains=query))
        return tasks


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'main/delete.html'
    success_url = reverse_lazy('home')


# def delete_page(self, pk):
#     print(self)
#     print(pk)
#     get_task = Task.objects.get(id=pk)
#     get_task.delete()
#     return redirect(reverse('home'))



# class DeleteTaskView(DeleteView):
#     model = Task
#     template_name = 'main/index.html'
#     success_url = reverse_lazy('home')
#
#     def deletetask(self, pk):
#         tasks = Task.objects.get(id=pk)
#         tasks.delete()
#         return redirect(reverse('home'))


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




