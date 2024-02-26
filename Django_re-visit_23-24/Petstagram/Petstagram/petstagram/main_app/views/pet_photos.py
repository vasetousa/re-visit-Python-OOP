from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse

from petstagram.main_app.helpers import BootstrapFormMixin, get_profile
from petstagram.main_app.models import PetPhoto, Pet
from petstagram.main_app.validators import validate_file_max_size_in_mb


class PetPhotoFormCreate(BootstrapFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = PetPhoto

        labels = {
            'photo': 'Pet Image',
            'description': 'Description',
            'tagged_pets': "Tag Pets",
        }
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter Description',
                    'rows': 3,
                }
            ),
        }
        fields = {'photo', 'description', 'tagged_pets'}


class PetPhotoFormEdit(BootstrapFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = PetPhoto

        labels = {
            'description': 'Description',
            'tagged_pets': "Tag Pets",
        }
        exclude = ['user_profile', ]
        fields = {'description', 'tagged_pets'}
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter Description',
                    'rows': 3,
                }
            ),
        }


def pet_photo_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        pet_photo_form = form_class(request.POST, request.FILES, instance=instance)
        if pet_photo_form.is_valid():
            pet_photo_form.save()
            return redirect(success_url)
    else:
        pet_photo_form = form_class(instance=instance)
    all_pet_photos = PetPhoto.objects.all()
    context = {
        'pet_photo_form': pet_photo_form,
        'hide_nav_items': False,
        'photo': instance,
    }

    return render(request, template_name, context)


def show_pet_photo_details(request, pk):
    pet_photo = (PetPhoto.objects.
                 prefetch_related('tagged_pets').
                 get(pk=pk))

    context = {
        'pet_photo': pet_photo
    }

    return render(request, 'photo_details.html', context)


def add_pet_photo(request):
    return pet_photo_action(request, PetPhotoFormCreate, 'dashboard', PetPhoto(),
                            'photo_create.html')


def edit_pet_photo(request, pk):
    # creating the URL before providing it, because of the pk
    success_url = reverse('pet photo details', kwargs={'pk': PetPhoto.objects.get(pk=pk).pk})
    return pet_photo_action(request, PetPhotoFormEdit, success_url, PetPhoto.objects.get(pk=pk),
                            'photo_edit.html')


def delete_pet_photo(request, pk):
    (PetPhoto.objects.get(pk=pk)).delete()
    return redirect('dashboard')


def like_pet_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()

    return redirect('pet photo details', pk)
