from django.contrib import admin

from MyMusicApp.base.models import Profile, Album


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'age')
    sortable_by = 'username'


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album_name', 'artist', 'genre')
    sortable_by = 'artist'
