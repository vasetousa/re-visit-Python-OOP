from django.urls import path

from petstagram.main_app.views.pets import CreatePetView, EditPetView, DeletePetView
from petstagram.main_app.views.profiles import show_profile, ProfileCreateView

from petstagram.main_app.views.pet_photos import show_pet_photo_details, edit_pet_photo, add_pet_photo, like_pet_photo, \
    delete_pet_photo

from petstagram.main_app.views.generic import HomeView, DashboardView, permission_denied

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    # """ profile operations """
    # ''' creating a profile after user register with a signal '''
    path('profile/', show_profile, name='profile'),
    # path('profile/create/', ProfileCreateView.as_view(), name='profile create'),

    # """ pet photos operations """
    path('photo/details/<int:pk>', show_pet_photo_details, name='pet photo details'),

    path('photo/add/', add_pet_photo, name='add pet photo'),
    path('photo/edit/<int:pk>/', edit_pet_photo, name='edit pet photo'),
    path('photo/delete/<int:pk>/', delete_pet_photo, name='delete pet photo'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo'),

    path('401/', permission_denied, {'exception': 'Unauthorized'}, name='unauthorized'),

    # """ pets operations """
    path('pet/create/', CreatePetView.as_view(), name='pet create'),
    path('pet/edit/<int:pk>/', EditPetView.as_view(), name='pet edit'),
    path('pet/delete/<int:pk>/', DeletePetView.as_view(), name='pet delete'),

)
