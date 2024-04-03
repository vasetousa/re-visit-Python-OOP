from django.urls import path

from Petstagram.main_app.views.generic import show_dashboard, permission_denied
from Petstagram.main_app.views.pet_photos import show_pet_photo_details, add_pet_photo, edit_pet_photo, \
    delete_pet_photo, like_pet_photo
from Petstagram.main_app.views.pets import pet_create, pet_edit, pet_delete
from Petstagram.main_app.views.profiles import show_profile, create_profile, edit_profile, delete_profile

urlpatterns = (
    path('dashboard/', show_dashboard, name='dashboard'),

    # """ profile operations """
    path('profile/', show_profile, name='profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

    # """ pet photos operations """
    path('photo/details/<int:pk>', show_pet_photo_details, name='pet photo details'),

    path('photo/add/', add_pet_photo, name='add pet photo'),
    path('photo/edit/<int:pk>/', edit_pet_photo, name='edit pet photo'),
    path('photo/delete/<int:pk>/', delete_pet_photo, name='delete pet photo'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo'),

    path('401/', permission_denied, {'exception': 'Unauthorized'}, name='unauthorized'),

    # """ pets operations """
    path('pet/create/', pet_create, name='pet create'),
    path('pet/edit/<int:pk>/', pet_edit, name='pet edit'),
    path('pet/delete/<int:pk>/', pet_delete, name='pet delete'),

)
