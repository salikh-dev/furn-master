from django import forms
from  django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from dataclasses import fields
from .models import *

User = get_user_model()

class Registration(UserCreationForm):
        username = forms.CharField(
                max_length=100,
                required=True,
                widget=forms.TextInput(attrs={
                "class": "form-control",
                "placeholder":"enter your username"
                })
        )
        email = forms.EmailField(
                required=True,
                widget=forms.TextInput(attrs={
                "class": "form-control",
                "placeholder":"enter your email addres"
                })
        )
        password1 = forms.CharField(
                max_length=50,
                required=True,
                widget=forms.PasswordInput(
                attrs={
                        "placeholder": "password",
                        'class': 'form-control',
                        'date-toggle': 'password',
                        'id':'password'
                }
                )
        )
        password2 = forms.CharField(
                max_length=50,
                required=True,
                widget=forms.PasswordInput(
                attrs={
                        "placeholder": "password confirmation",
                        'class': 'form-control',
                        'date-toggle': 'password',
                        'id':'password'
                }
                )
        )
        class Meta:
                model = User
                fields= ["username", "email", "password1","password2"]