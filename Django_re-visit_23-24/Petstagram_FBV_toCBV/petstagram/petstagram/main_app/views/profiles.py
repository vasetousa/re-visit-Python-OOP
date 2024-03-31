from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic as views

from petstagram.main_app.forms import ProfileCreateForm
from petstagram.main_app.models import PetPhoto, Pet
from petstagram.main_app.helpers import get_profile


def show_profile(request):
    total_likes = 0
    profile = get_profile()
    pet_photos = set(PetPhoto.objects.all())
    count = PetPhoto.objects.count()
    for like in pet_photos:
        total_likes += like.likes
    context = {
        'profile': profile,
        'pets': Pet.objects.all(),
        'pet_photos': pet_photos,
        'count': count,
        'total_likes': total_likes
    }
    return render(request, 'main/profile_details.html', context)


# def profile_action(request, form_class, success_url, instance, template_name):
#     if request.method == 'POST':
#         profile_form = form_class(request.POST, instance=instance)
#         if profile_form.is_valid():
#             profile_form.save()
#             return redirect(success_url)
#     else:
#         profile_form = form_class(instance=instance)
#
#     context = {
#         'profile_form': profile_form,
#         'hide_nav_items': True,
#         'profile': instance,
#     }
#
#     return render(request, template_name, context)


class ProfileCreateView(LoginRequiredMixin, views.CreateView):
    template_name = 'main/profile_create.html'
    form_class = ProfileCreateForm



# def create_profile(request):
#     return profile_action(request, ProfileCreateForm, 'home', Profile(), 'main/profile_create.html')

#
# def edit_profile(request):
#     return profile_action(request, ProfileEditForm, 'profile', get_profile(), 'main/profile_edit.html')
#
#
# def delete_profile(request):
#     return profile_action(request, ProfileDeleteForm, 'home', get_profile(), 'main/profile_delete.html')
