from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from django.views import generic as views

from petstagram.main_app.helpers import get_profile
from petstagram.main_app.models import PetPhoto


class HomeView(views.TemplateView):
    template_name = 'main/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_nav_items'] = True
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')

        return super().dispatch(request, *args, **kwargs)


class DashboardView(views.ListView):
    model = PetPhoto
    template_name = 'main/dashboard.html'
    context_object_name = 'pet_photos'


def permission_denied(request):
    profile = get_profile()

    if not profile:
        raise PermissionDenied
    return redirect('unauthorized')
