from django.urls import path

from MyMusicApp.base.home_view.views import HomeView
from MyMusicApp.base.views import ProfileView, AlbumCreateView, AlbumDetailsView, ProfileDeleteView, ProfileEditView, \
    AlbumEditView, AlbumDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home-page'),

    path('profile/details/', ProfileView.as_view(), name='profile details'),
    path('profile/delete/<int:pk>/', ProfileDeleteView.as_view(), name='profile delete'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile edit'),

    path('album/add/', AlbumCreateView.as_view(), name='album add'),
    path('album/edit/<int:pk>/', AlbumEditView.as_view(), name='album edit'),
    path('album/delete/<int:pk>/', AlbumDeleteView.as_view(), name='album delete'),
    path('album/details/<int:pk>/', AlbumDetailsView.as_view(), name='album details'),
]
