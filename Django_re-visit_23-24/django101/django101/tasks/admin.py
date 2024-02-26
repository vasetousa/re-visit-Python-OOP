from django.contrib import admin

from django101.tasks.models import Task

# Register your models here.

# 1 same as 2
# admin.site.register(Task)


# 2
'''
How to show tables in admin. Decorating admin side
'''


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('title',)
    sortable_by = ('title',)
