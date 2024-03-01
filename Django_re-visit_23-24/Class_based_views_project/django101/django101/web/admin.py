from django.contrib import admin

from django101.web.models import Todo, Category


# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
