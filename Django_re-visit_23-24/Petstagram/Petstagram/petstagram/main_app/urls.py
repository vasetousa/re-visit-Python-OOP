from django.urls import path
from petstagram.main_app.views import home, show_dashboard, show_profile, show_pet_photo_details, like_pet_photo

urlpatterns = [
    path('', home, name='index'),
    path('profile/', show_profile, name='profile'),
    path('dashboard/', show_dashboard, name='dashboard'),
    path('photo/details/<int:pk>', show_pet_photo_details, name='pet_photo_details'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo'),
]
