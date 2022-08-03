from django import forms
from  django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from dataclasses import fields
from .models import *

User = get_user_model()

class Registration(UserCreationForm):
     class Meta:
        model = User
        fields=("username","first_name", "last_name", "email")
        field_classes = {"username": UsernameField}
# class Registration(forms.ModelForm):
#     first_name = forms.CharField(
#         max_length=100,
#         required=True,
#         widget=forms.TextInput(attrs={
#             "class": "form-control",
#             "placeholder":"ismingizni kirting"
#         })
#     )
#     last_name = forms.CharField(
#         max_length=100,
#         required=True,
#         widget=forms.TextInput(attrs={
#             "class": "form-control",
#             "placeholder":"familyangizni kirting"
#         })
#     )
#     email = forms.EmailField(
#         required=True,
#         widget=forms.TextInput(attrs={
#             "class": "form-control",
#             "placeholder":"emailimgizni kiritng kirting"
#         })
#     )
#     password1 = forms.CharField(
#         max_length=50,
#         required=True,
#         widget=forms.PasswordInput(
#             attrs={
#                 "placeholder": "password",
#                 'class': 'form-control',
#                 'date-toggle': 'password',
#                 'id':'password'
#             }
#         )
#     )
#     password2 = forms.CharField(
#         max_length=50,
#         required=True,
#         widget=forms.PasswordInput(
#             attrs={
#                 "placeholder": "password",
#                 'class': 'form-control',
#                 'date-toggle': 'password',
#                 'id':'password'
#             }
#         )
#     )

#     username = None

#     class Meta:
#         model = User
#         fields=["first_name", "last_name", "email", "password1", "password2"]