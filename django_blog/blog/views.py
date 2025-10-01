from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PostForm


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

# List all blog posts
class PostListView(ListView):
    """
    Displays a list of all blog posts.
    """
    model = Post
    template_name = 'blog/post_list.html'  # Custom template
    context_object_name = 'posts'
    ordering = ['-created_at']  # Newest posts first

# Display details of a single blog post
class PostDetailView(DetailView):
    """
    Displays details of a single blog post.
    """
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# Create a new blog post (authenticated users only)
class PostCreateView(LoginRequiredMixin, CreateView):
    """
    Allows authenticated users to create a new post.
    """
    model = Post
    form_class = PostForm   
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        """
        Assign the logged-in user as the author before saving the form.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# Update an existing blog post (only by the author)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Allows the author of the post to update it.
    """
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        """
        Ensure the logged-in user is the author.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        Checks if the logged-in user is the author of the post.
        """
        post = self.get_object()
        return self.request.user == post.author

# Delete an existing blog post (only by the author)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Allows the author to delete their post.
    """
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        """
        Checks if the logged-in user is the author of the post.
        """
        post = self.get_object()
        return self.request.user == post.author