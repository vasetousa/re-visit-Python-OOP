from django.contrib.auth.views import LogoutView
from django.urls import path

from Tasks.base.account_views.views import CustomLoginView, RegisterPage
from Tasks.base.task_views.views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = (
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', TaskListView.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task'),
    path('task-create/', TaskCreateView.as_view(), name='task create'),
    path('task-update/<int:pk>/', TaskUpdateView.as_view(), name='task update'),
    path('task-delete/<int:pk>/', TaskDeleteView.as_view(), name='task delete'),
)
