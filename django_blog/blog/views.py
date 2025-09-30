from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.forms import UserCreationForm


# --- Create a Profile Form ---
class ProfileForm(forms.ModelForm):
    """
    A form for updating user profile information.
    Currently allows editing email, first_name, and last_name.
    Can be extended with more fields later (e.g., profile picture, bio).
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


# --- Profile View ---
@login_required  # ✅ Only logged-in users can access
def profile(request):
    """
    Handle profile management:
    - GET → show the form with current user info
    - POST → update the user’s information
    """
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully.")
            return redirect("profile")  # reload page after saving
    else:
        form = ProfileForm(instance=request.user)

    return render(request, "blog/profile.html", {"form": form})

def home(request):
    return render(request, "blog/home.html")

def post_list(request):
    posts = Post.objects.all().order_by("-published_date")  # fetch all posts
    return render(request, "blog/post_list.html", {"posts": posts})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created! You can now log in.")
            return redirect("login")  # make sure you have a 'login' URL
    else:
        form = UserCreationForm()
    return render(request, "blog/register.html", {"form": form})
