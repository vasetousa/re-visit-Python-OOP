from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from Tasks.base.models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    template_name = 'tasks_list.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(user=self.request.user)
        context['count'] = context['tasks'].filter(completed=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__startswith=search_input
            )

        context['search_input'] = search_input
        return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_detail.html'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'task_create.html'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task_update.html'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')

    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     # Disable the 'title' field
    #     form.fields['title'].disabled = True
    #     return form


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_delete.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')
