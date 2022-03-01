from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db.models import fields
from .models import Music, Contact


class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ("music_file", "artist", "composer", "lyricist")


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
