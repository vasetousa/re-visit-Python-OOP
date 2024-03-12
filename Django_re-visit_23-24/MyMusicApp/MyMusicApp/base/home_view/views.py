from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView

from MyMusicApp.base.models import Profile, Album
from MyMusicApp.base.views import ProfileCreateView, ProfileCreateForm


class HomeView(TemplateView):
    def get_template_names(self):

        if Profile.objects.first():
            return ['home-with-profile.html']
        else:
            return ['home-no-profile.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['albums'] = Album.objects.all()
        context['profile_form'] = ProfileCreateForm()
        return context

    def post(self, request, *args, **kwargs):
        profile_form = ProfileCreateForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('home-page')
        print(profile_form.errors)
        context = {'profile_form': profile_form}
        return render(request, 'home-no-profile.html', context)
