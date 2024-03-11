from django.urls import reverse_lazy
from django.views import generic as views

from django.shortcuts import render

from django101.web.models import Todo


# Create your views here.

def contacts(request):
    return render(request, 'contact.html')


def show_index(request):
    context = {
        'title': 'Func based views'
    }

    return render(request, 'index.html', context)


class IndexView(views.View):
    def get(self, request):
        context = {
            'title': 'Class based views'
        }
        return render(request, 'index.html', context)


class TodosListView(views.ListView):
    model = Todo
    template_name = 'todos_list_view.html'
    context_object_name = 'Todos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TodosDetailView(views.DetailView):
    model = Todo
    template_name = 'todo_details.html'


class TodosCreateView(views.CreateView):
    model = Todo
    fields = '__all__'
    template_name = 'todo_create.html'
    success_url = reverse_lazy('todos list')


class TodosUpdateView(views.UpdateView):
    model = Todo
    fields = '__all__'
    template_name = 'todo_update.html'
    success_url = reverse_lazy('todos list')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        return obj


class TodosDeleteView(views.DeleteView):
    model = Todo
    template_name = 'todo_delete.html'
    success_url = reverse_lazy('todos list')
