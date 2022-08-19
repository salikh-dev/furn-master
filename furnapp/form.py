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


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        # widgets = {
        #     'first_name':forms.TextInput(attrs={"class": "form-control","placeholder":"First Name", "id":'firstname', "value":"user"}),
        #     'last_name':forms.TextInput(attrs={"class": "form-control", "placeholder":"Last Name", "id":"lastname"})
        # }