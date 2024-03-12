from django.urls import path
from djangoExam.mymusicapp.views import *

urlpatterns = [
    path('', home_page, name='home-page'),
    path('album/add/', add_album, name='add-album'),
    path('album/details/<int:album_id>/', show_album_details, name='one-album-details'),
    path('album/edit/<int:album_id>/', edit_album, name='edit-album'),
    path('delete-album/<int:album_id>/', delete_album, name='delete-album'),
    path('profile/', show_profile, name='profile-page'),
    path('profile/delete', delete_profile, name='delete-profile'),
]
