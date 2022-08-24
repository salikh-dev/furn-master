from django import forms
from  django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm
from django.contrib.auth import get_user_model
from dataclasses import fields
from .models import *

User = get_user_model()

class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]


# class EditProfileForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', "email"]
#         widgets = {
#             'first_name':forms.TextInput(attrs={"class": "form-control","placeholder":"First Name", "id":'firstname', "value":"user"}),
#             'last_name':forms.TextInput(attrs={"class": "form-control", "placeholder":"Last Name", "id":"lastname"}),
#             'email':forms.EmailInput(attrs={"class":'form-control w-75', "placeholder":"Email", "id":"email"})
#         }

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', "email"]
        widgets = {
            'first_name':forms.TextInput(attrs={"class": "form-control","placeholder":"First Name", "id":'firstname', "value":"user"}),
            'last_name':forms.TextInput(attrs={"class": "form-control", "placeholder":"Last Name", "id":"lastname"}),
            'email':forms.EmailInput(attrs={"class":'form-control w-75', "placeholder":"Email", "id":"email"})
        }


class UpdateProfileForm(forms.ModelForm):
    image = forms.CharField(widget=forms.FileInput(
        attrs={'class':'form-control'}
    ))
    bio = forms.CharField(widget=forms.TextInput(
            attrs={'class':'form-control'}
        )
    )
    card_number = forms.CharField(widget=forms.TextInput(
            attrs={'class':'form-control'}
        )
    )
    address = forms.CharField(widget=forms.TextInput(
            attrs={'class':'form-control'}
        )
    )
    telephone = forms.CharField(widget=forms.TextInput(
            attrs={'class':'form-control'}
        )
    )
    skill = forms.CharField(widget=forms.TextInput(
            attrs={'class':'form-control'}
        )
    )
    hobbies = forms.CharField(widget=forms.TextInput(
            attrs={'class':'form-control'}
        )
    )
    facebook = forms.CharField(widget=forms.TextInput(
            attrs={'class':'form-control'}
        )
    )
    telegram = forms.CharField(widget=forms.TextInput(
            attrs={'class':'form-control'}
        )
    )
    instagram = forms.CharField(widget=forms.TextInput(
            attrs={'class':'form-control'}
        )
    )
    twitter = forms.CharField(widget=forms.TextInput(
            attrs={'class':'form-control'}
        )
    )
    snapchat = forms.CharField(widget=forms.TextInput(
            attrs={'class':'form-control'}
        )
    )
    github = forms.CharField(widget=forms.TextInput(
            attrs={'class':'form-control'}
        )
    )
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'card_number', 'address', 'telephone', 'telephone', 'skill', 'hobbies', 'facebook', 'telegram', 'instagram', 'twitter', 'snapchat', 'github']
        # fields = '__all__'


