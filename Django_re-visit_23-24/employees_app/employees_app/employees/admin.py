from django.contrib import admin

from employees_app.employees.models import Employee, Department


# Register your models here.
@admin.register(Employee)
class AdminEmployee(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'department', 'email', 'job_title', 'company', 'egn')
    list_filter = ('last_name', 'first_name',)
    sortable_by = ('last_name',)


@admin.register(Department)
class AdminDepartment(admin.ModelAdmin):
    list_display = ('name',)

