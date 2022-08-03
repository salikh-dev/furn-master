from django import forms
from  django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from dataclasses import fields

User = get_user_model()


# class Registration(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ("username",)
#         field_classes = {"username":UsernameField}


class Registration(forms.ModelForm):
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeolder":"ismingizni kirting"
        })
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeolder":"familyangizni kirting"
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeolder":"emailimgizni kiritng kirting"
        })
    )
    password1 = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeolder": "password",
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
                "placeolder": "password",
                'class': 'form-control',
                'date-toggle': 'password',
                'id':'password'
            }
        )
    )

    class Meta:
        model = User
        fields("first_name", "last_name", "email", "password1", "password2")
        field_classes = {"username":UsernameField}