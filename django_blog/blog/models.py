from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

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
    
class Comment(models.Model):
    """
    Model representing a comment made by a user on a blog post.

    Fields:
        post (ForeignKey): The post this comment belongs to.
        author (ForeignKey): The user who wrote the comment.
        content (TextField): The text content of the comment.
        created_at (DateTimeField): Timestamp when the comment was created.
        updated_at (DateTimeField): Timestamp when the comment was last updated.
    """

    post = models.ForeignKey(
        'Post', 
        on_delete=models.CASCADE, 
        related_name='comments',
        help_text='The post that this comment belongs to.'
    )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='comments',
        help_text='The user who authored this comment.'
    )
    content = models.TextField(
        help_text='The content of the comment.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text='The date and time when the comment was created.'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text='The date and time when the comment was last updated.'
    )

    class Meta:
        ordering = ['created_at']  # Comments will be ordered chronologically
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'



