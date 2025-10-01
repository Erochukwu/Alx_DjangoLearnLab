from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    """
    Represents a blog post created by a user.
    """
    title = models.CharField(max_length=200, help_text="Enter the title of the post")
    content = models.TextField(help_text="Write the content of your post here")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String representation of the Post model
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the URL to access a detail view of this post.
        """
        return reverse('post_detail', args=[str(self.id)])

