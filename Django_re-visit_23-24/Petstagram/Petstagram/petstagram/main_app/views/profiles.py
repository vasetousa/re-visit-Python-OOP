from django import forms
from django.shortcuts import render, redirect

from petstagram.main_app.models import Profile, PetPhoto, Pet
from petstagram.main_app.helpers import get_profile, BootstrapFormMixin


class ProfileCreateForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        # fields = "__all__"
        fields = ['first_name', 'last_name', 'picture']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name'
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name'
                }
            ),

            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL'
                }
            )
        }


class ProfileEditForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        fields = "__all__"
        # fields = ['first_name', 'last_name', 'picture']
        widgets = {
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Enter email'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter description',
                    'rows': 3
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'date_of_birth': forms.DateInput(
                        attrs={
                            'min': '1920-01-01',
                        }
                    )
                }
            ),
        }





# class DateChoiceForm(forms.Form):
#     selected_date = forms.DateField(widget=forms.SelectDateWidget)
#

class ProfileDeleteForm(forms.ModelForm):

    def save(self, commit=True):
        pets = list(self.instance.pet_set.all())
        pet_photos = PetPhoto.objects.filter(tagged_pets__in=pets)
        pet_photos.delete()
        self.instance.delete()

        return self.instance

    class Meta:
        model = Profile
        fields = ()


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
    return render(request, 'profile_details.html', context)


def profile_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        profile_form = form_class(request.POST, instance=instance)
        if profile_form.is_valid():
            profile_form.save()
            return redirect(success_url)
    else:
        profile_form = form_class(instance=instance)

    context = {
        'profile_form': profile_form,
        'hide_nav_items': True,
        'profile': instance,
    }

    return render(request, template_name, context)


def create_profile(request):
    return profile_action(request, ProfileCreateForm, 'home', Profile(), 'profile_create.html')


def edit_profile(request):
    return profile_action(request, ProfileEditForm, 'profile', get_profile(), 'profile_edit.html')


def delete_profile(request):
    return profile_action(request, ProfileDeleteForm, 'home', get_profile(), 'profile_delete.html')
