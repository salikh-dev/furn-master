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

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', "email"]
        widgets = {
            'first_name':forms.TextInput(attrs={"class": "form-control","placeholder":"First Name", "id":'firstname', "value":"user"}),
            'last_name':forms.TextInput(attrs={"class": "form-control", "placeholder":"Last Name", "id":"lastname"}),
            'email':forms.EmailInput(attrs={"class":'form-control w-75', "placeholder":"Email", "id":"email"})
        }


class UpdateprofileForm(forms.ModelForm):
    image = forms.CharField(widget=forms.FileInput(
        attrs={'class':'form-control'}
    ))
    bio = forms.CharField(widget=forms.TextInput(
            attrs={'class':'form-control'}
        )
    )
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'card_number', 'address', 'telephone', 'job', 'skill', 'hobbies', 'facebook', 'telegram', 'instagram', 'twitter', 'snapchat', 'github']
        # fields = '__all__'


