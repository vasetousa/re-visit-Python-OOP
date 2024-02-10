from django import template

from employees_app.employees.models import Department

register = template.Library()


@register.inclusion_tag('tags/departmentss_list.html')
def departmentss_list():
    departmentss = Department.objects.prefetch_related('employee_set').all()


    # context
    return {
        'departmentss': departmentss,
    }
