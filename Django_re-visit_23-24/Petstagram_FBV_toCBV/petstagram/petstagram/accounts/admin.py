from django.contrib import admin

from petstagram.accounts.models import PetstagramUser
from petstagram.main_app.models import Pet


# Register your models here.
@admin.register(PetstagramUser)
class PetstagramUserAdmin(admin.ModelAdmin):
    list_display = ('username',)
