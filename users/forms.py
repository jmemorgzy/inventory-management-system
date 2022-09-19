from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=101)

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
