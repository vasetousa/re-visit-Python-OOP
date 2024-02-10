from django.urls import path

from employees_app.employees.views import create_employee, log_in, employees_list, edit_employee

urlpatterns = [
    path('employees/create/', create_employee, name='create employee'),
    path('login', log_in, name='log in'),
    path('employees/list/', employees_list, name='employees list'),
    path('employees/edit/<int:pk>/', edit_employee, name='edit employee'),
    # path('employee/update/', update_employee, name='update employee'),
    # path('create/', create_department, name='create department'),
    # path('update/', update_department, name='update department'),
]
