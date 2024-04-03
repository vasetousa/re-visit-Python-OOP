from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render

from Petstagram.main_app.helpers import get_profile
from Petstagram.main_app.models import PetPhoto


# def error_401(request):
#     profile = get_profile()
#     if profile is None:
#         return redirect('error 401')


def home(request):
    context = {
        'hide_nav_items': True,
    }
    return render(request, 'home_page.html', context)


def show_dashboard(request):
    profile = get_profile()
    if not profile:
        return redirect('home')

    pet_photos = set(PetPhoto.objects.
                     prefetch_related('tagged_pets').
                     filter(tagged_pets__user_profile=profile))
    context = {
        'pet_photos': pet_photos
    }
    return render(request, 'dashboard.html', context)


def permission_denied(request):
    profile = get_profile()

    if not profile:
        raise PermissionDenied
    return redirect('unauthorized')