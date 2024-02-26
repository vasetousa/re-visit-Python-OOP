import datetime
from datetime import date

from django import forms
from django.shortcuts import render, redirect

from petstagram.main_app.helpers import BootstrapFormMixin, get_profile, DisabledFieldsFormMixin
from petstagram.main_app.models import Pet


class PetFormCreate(BootstrapFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Pet
        fields = {'name', 'type', 'date_of_birth'}
        labels = {
            'date_of_birth': 'Day of Birth',
            'name': 'Pet Name',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter pet name',
                }
            )
        }



class PetFormEdit(BootstrapFormMixin, forms.ModelForm):
    MIN_DATE_OF_BIRTH = date(1920, 1, 1)
    MAX_DATE_OF_BIRTH = date.today()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth is None:
            return date_of_birth
        if date_of_birth < self.MIN_DATE_OF_BIRTH or self.MAX_DATE_OF_BIRTH < date_of_birth:
            raise forms.ValidationError(
                f'Date of birth must be between {self.MIN_DATE_OF_BIRTH} and {self.MAX_DATE_OF_BIRTH}')
        return date_of_birth

    class Meta:
        model = Pet
        labels = {
            'date_of_birth': 'Day of Birth',
            'name': 'Pet Name',
        }
        fields = {'name', 'type', 'date_of_birth'}
        exclude = ['user_profile', ]


class PetFormDelete(BootstrapFormMixin, DisabledFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    class Meta:
        model = Pet
        exclude = ['user_profile', ]

    def save(self, commit=True):
        self.instance.delete()
        return self.instance


def pet_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        pet_form = form_class(request.POST, instance=instance)
        if pet_form.is_valid():
            pet_form.save()
            return redirect(success_url)
    else:
        pet_form = form_class(instance=instance)
    pets = Pet.objects.all()
    context = {
        'pet_form': pet_form,
        'hide_nav_items': False,
        'all_pets': pets,
        'pet': instance,
    }

    return render(request, template_name, context)


def pet_create(request):
    return pet_action(request, PetFormCreate, 'profile', Pet(user_profile=get_profile()), 'pet_create.html')


def pet_edit(request, pk):
    return pet_action(request, PetFormEdit, 'profile', Pet.objects.get(pk=pk), 'pet_edit.html')


def pet_delete(request, pk):
    return pet_action(request, PetFormDelete, 'profile', Pet.objects.get(pk=pk), 'pet_delete.html')
