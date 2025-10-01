from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post


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

class PostForm(forms.ModelForm):
    """
    Form for creating and updating blog posts.

    Fields:
        - title: The title of the blog post.
        - content: The content/body of the blog post.
    
    The author field is automatically set in the view based on the logged-in user.
    """

    class Meta:
        model = Post
        fields = ['title', 'content']  # Exclude 'author'; set automatically
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your post content here...',
                'rows': 5
            }),
        }

    def clean_title(self):
        """
        Validate that the title is not empty and is at least 5 characters long.
        """
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title

    def clean_content(self):
        """
        Validate that the content is not empty.
        """
        content = self.cleaned_data.get('content')
        if not content.strip():
            raise forms.ValidationError("Content cannot be empty.")
        return content
