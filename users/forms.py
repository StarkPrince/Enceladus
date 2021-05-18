from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_crispy_bulma.forms import EmailField
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = EmailField(
        label="email",
        required=True
    )
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = EmailField(
        label="email",
        required=True
    )
    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    email = EmailField(
        label="email",
        required=True
    )
    class Meta:
        model = Profile
        fields = ['image']