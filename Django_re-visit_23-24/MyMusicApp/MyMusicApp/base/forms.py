from django import forms

from MyMusicApp.base.models import Profile, Album


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),
            'age': forms.TextInput(
                attrs={'placeholder': 'Age'
                       }
            ),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age']

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['username'].disabled = True  # Disable editing username field


class AlbumCreateForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name'
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist'
                }
            ),
            'description': forms.Textarea(
                attrs={'placeholder': 'Description',
                       'rows': '3'
                       }
            ),
            'image_url': forms.TextInput(
                attrs={'placeholder': 'Image URL'
                       }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Price'
                }
            )
        }


class AlbumEditForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class AlbumDeleteForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AlbumDeleteForm, self).__init__(*args, **kwargs)
        self.fields['album_name'].disabled = True  # Disable editing username field
        self.fields['artist'].disabled = True
        self.fields['genre'].disabled = True
        self.fields['description'].disabled = True
        self.fields['image_url'].disabled = True
        self.fields['price'].disabled = True