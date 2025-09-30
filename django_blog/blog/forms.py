from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    """
    Custom registration form that extends Django's built-in UserCreationForm.
    Adds an email field so users can register with their email address.
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        # Fields to display in the registration form
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    """
    A form for updating user profile info.
    Currently allows editing only email.
    Can be extended to include more fields.
    """
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]