from django.urls import path

from employees_app.employees.views import department, department_list, department_details, create_department, \
    update_department, delete_department

urlpatterns = [
    path('<int:id>/', department), # http://127.0.0.1:8000/departments/66/ id=66
    path('list/', department_list),
    path('details/', department_details),
    path('create/', create_department),
    path('update/', update_department),
    path('delete/', delete_department),
]
