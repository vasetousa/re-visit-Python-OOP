from django.urls import path

from django101.web.views import IndexView, show_index, TodosListView, TodosDetailView, TodosCreateView, TodosUpdateView, \
    TodosDeleteView

urlpatterns = (
    path('cbv/', IndexView.as_view(), name='IndexView'),
    path('fbv/', show_index, name='show_index'),
    path('todos/', TodosListView.as_view(), name='todos list'),
    path('todos/<int:pk>/', TodosDetailView.as_view(), name='todo details'),
    path('todos/create/', TodosCreateView.as_view(), name='todo create'),
    path('todos/update/<int:pk>/', TodosUpdateView.as_view(), name='todo update'),
    path('todos/delete/<int:pk>/', TodosDeleteView.as_view(), name='todo delete'),
)