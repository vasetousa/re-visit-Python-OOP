from django.shortcuts import render, redirect
from django.views import generic as views

from petstagram.main_app.forms import PetFormCreate, PetFormEdit, PetFormDelete
from petstagram.main_app.helpers import get_profile
from petstagram.main_app.models import Pet


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


class CreatePetView(views.CreateView):
    template_name = 'main/pet_create.html'
    form_class = PetFormCreate

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditPetView(views.UpdateView):
    template_name = 'main/pet_edit.html'
    form_class = PetFormEdit


class DeletePetView(views.DeleteView):
    template_name = 'main/pet_delete.html'
    form_class = PetFormDelete
