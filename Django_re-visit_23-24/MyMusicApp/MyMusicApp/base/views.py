from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView

from MyMusicApp.base.forms import ProfileCreateForm, AlbumCreateForm, ProfileEditForm, AlbumEditForm, AlbumDeleteForm
from MyMusicApp.base.models import Profile, Album
from django.views.generic import TemplateView


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm  # Use your form class here
    template_name = 'home-no-profile.html'
    success_url = '/home-page/'

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = None

    def form_valid(self, form):
        # You can customize any additional logic here

        self.object = form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.first()
        context['profile'] = profile
        context['profile_form'] = ProfileCreateForm()
        return context


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm  # Use your form class here
    template_name = 'profile-edit.html'

    '''variant 1'''

    def get_initial(self):
        initial = super().get_initial()
        profile = self.get_object()
        initial['username'] = profile.username
        initial['email'] = profile.email
        initial['age'] = profile.age
        return initial

    '''variant 2'''

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     profile = self.get_object()
    #     kwargs['initial'] = {
    #         'username': profile.username,
    #         'email': profile.email,
    #         'age': profile.age
    #     }
    #     return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        profile_form = self.get_form()  # Retrieve the form instance
        context['profile'] = profile
        context['profile_form'] = profile_form
        return context

    def get_success_url(self):
        return reverse_lazy('profile details')


class ProfileView(TemplateView):
    template_name = 'profile-details.html'

    def get_context_data(self, **kwargs):
        profile = Profile.objects.first()
        context = super().get_context_data(**kwargs)
        context['profile'] = profile
        context['albums_count'] = len(Album.objects.all())
        return context


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profile-delete.html'

    def get_success_url(self):
        return reverse_lazy('home-page')


class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumCreateForm  # Use your form class here
    template_name = 'add-album.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile = Profile.objects.first()
        context['profile'] = profile
        context['album_form'] = AlbumCreateForm()
        return context

    def get_success_url(self):
        return reverse_lazy('home-page')


class AlbumDetailsView(DetailView):
    model = Album
    template_name = 'album-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        albums = Album.objects.filter(pk=self.kwargs['pk'])
        profile = Profile.objects.first()
        context['profile'] = profile
        context['albums'] = albums

        return context


class AlbumEditView(UpdateView):
    model = Album
    form_class = AlbumEditForm
    template_name = 'edit-album.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        album = self.get_object()
        kwargs['initial'] = {
            'album_name': album.album_name,
            'artist': album.artist,
            'genre': album.genre,
            'description': album.description,
            'image_url': album.image_url,
            'price': album.price,
        }
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile = Profile.objects.first()
        profile_form = self.get_form()  # Retrieve the form instance
        context['profile_form'] = profile_form
        context['profile'] = profile
        return context

    def get_success_url(self):
        return reverse_lazy('album details', kwargs={'pk': self.kwargs['pk']})


class AlbumDeleteView(DeleteView):
    model = Album
    form_class = AlbumDeleteForm
    template_name = 'delete-album.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        album = self.get_object()
        kwargs['initial'] = {
            'album_name': album.album_name,
            'artist': album.artist,
            'genre': album.genre,
            'description': album.description,
            'image_url': album.image_url,
            'price': album.price,
        }
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile = Profile.objects.first()
        profile_form = self.get_form()  # Retrieve the form instance
        context['profile_form'] = profile_form
        context['profile'] = profile
        return context

    def get_success_url(self):
        return reverse_lazy('home-page')

    def post(self, request, *args, **kwargs):
        # Get the album object to be deleted
        album = self.get_object()
        album.delete()
        return redirect(reverse_lazy('home-page'))