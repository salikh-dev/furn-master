from django import forms
from  django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from dataclasses import fields

User = get_user_model()


class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ("username")
        field_classes = {"username":UsernameField}

