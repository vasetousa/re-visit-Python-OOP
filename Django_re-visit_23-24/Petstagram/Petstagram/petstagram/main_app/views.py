from django.shortcuts import render, redirect

from petstagram.main_app.models import Profile, Pet, PetPhoto


# Create your views here.

def get_profile():
    prof = Profile.objects.all()
    if prof:
        return prof[0]
    return None


def home(request):
    context = {
        'hide_nav_items': True,
    }
    return render(request, 'main_app/home_page.html', context)


def show_dashboard(request):
    profile = get_profile()
    pet_photos = set(PetPhoto.objects.
                     prefetch_related('tagged_pets').
                     filter(tagged_pets__user_profile=profile))
    context = {
        'pet_photos': pet_photos
    }
    return render(request, 'main_app/dashboard.html', context)


def show_profile(request):
    total_likes = 0
    profile = get_profile()
    pet_photos = set(PetPhoto.objects.all())
    count = PetPhoto.objects.count()
    for like in pet_photos:
        total_likes += like.likes
    context = {
        'profile': profile,
        'pet_photos': pet_photos,
        'count': count,
        'total_likes': total_likes
    }
    return render(request, 'main_app/profile_details.html', context)


def show_pet_photo_details(request, pk):
    pet_photo = (PetPhoto.objects.
                 prefetch_related('tagged_pets').
                 get(pk=pk))

    context = {
        'pet_photo': pet_photo
    }

    return render(request, 'main_app/photo_details.html', context)


def like_pet_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()

    return redirect('pet_photo_details', pk)







# https://images.unsplash.com/photo-1623387641168-d9803ddd3f35?ixlib=rb-
# 1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8cGV0c3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60

# https://icon-library.com/images/profile-picture-icon/profile-picture-icon-9.jpg

# https://images.unsplash.com/photo-1623387641168-
# d9803ddd3f35?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8cGV0c3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60
