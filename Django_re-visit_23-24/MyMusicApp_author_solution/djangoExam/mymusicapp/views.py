from django.shortcuts import render, redirect

from djangoExam.mymusicapp.forms import CreateProfileForm, CreateAlbumForm, DeleteAlbumForm
from djangoExam.mymusicapp.models import Profile, Album


def home_page(request):
    try:
        profile = Profile.objects.all()[0]
        context = {
            'profile': profile,
            'albums': Album.objects.all(),
        }
        return render(request, 'mymusicapp/home-with-profile.html', context=context)
    except IndexError:
        if request.method == 'POST':
            form = CreateProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home-page')
            context = {'form': form}
            return render(request, 'mymusicapp/home-no-profile.html', context)
        form = CreateProfileForm()
        context = {'form': form}
        return render(request, 'mymusicapp/home-no-profile.html', context)


def add_album(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
        context = {'form': form, 'profile': profile}
        return render(request, 'mymusicapp/add-album.html', context)
    form = CreateAlbumForm()
    context = {'form': form, 'profile': profile}
    return render(request, 'mymusicapp/add-album.html', context)


def show_album_details(request, album_id):
    album = Album.objects.get(id=album_id)
    context = {'album': album}
    return render(request, 'mymusicapp/album-details.html', context)


def edit_album(request, album_id):
    album = Album.objects.get(id=album_id)
    if request.method == "GET":
        context = {'form': CreateAlbumForm(initial=album.__dict__)}
        return render(request, 'mymusicapp/edit-album.html', context)
    else:
        form = CreateAlbumForm(request.POST, instance=album)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('home-page')
        else:
            context = {'form': form}
            return render(request, 'mymusicapp/edit-album.html', context)


def delete_album(request, album_id):
    album = Album.objects.get(id=album_id)
    if request.method == 'POST':
        album.delete()
        return redirect('home-page')

    form = DeleteAlbumForm(instance=album)
    context = {'form': form, 'profile': Profile.objects.first()}
    return render(request, 'mymusicapp/delete-album.html', context)


def show_profile(request):
    profile = Profile.objects.first()
    all_albums = len(Album.objects.all())
    context = {'profile': profile, 'all_albums': all_albums}
    return render(request, 'mymusicapp/profile-details.html', context)


def delete_profile(request):
    if request.method == 'POST':
        profile = Profile.objects.first()
        profile.delete()
        Album.objects.all().delete()
        return redirect('home-page')
    return render(request, 'mymusicapp/profile-delete.html')
