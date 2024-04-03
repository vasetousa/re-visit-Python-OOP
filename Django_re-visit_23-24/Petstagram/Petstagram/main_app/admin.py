from django.contrib import admin

from Petstagram.main_app.models import Pet, Profile, PetPhoto


# Register your models here.




# Register your models here.

# shows pets in the profile
class PetInlineAdmin(admin.StackedInline):
    model = Pet


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'gender', 'date_of_birth')
    list_filter = ('last_name', 'first_name',)
    sortable_by = ('last_name', 'first_name',)
    inlines = [PetInlineAdmin]


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_of_birth')


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    pass
