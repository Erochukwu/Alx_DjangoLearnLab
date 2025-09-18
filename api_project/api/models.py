from django.db import models

class Book(models.Model):
    """
    The Book model represents a simple resource for our API.
    It stores basic information about a book, including its title and author.

    Fields:
        title (CharField): The title of the book (max length 200 characters).
        author (CharField): The author of the book (max length 100 characters).
    """

    title = models.CharField(
        max_length=200,
        help_text="Enter the title of the book (e.g. 'To Kill a Mockingbird')."
    )
    author = models.CharField(
        max_length=100,
        help_text="Enter the author's full name (e.g. 'Harper Lee')."
    )

    def __str__(self):
        """
        Returns a human-readable string representation of the book.
        Example: 'To Kill a Mockingbird by Harper Lee'
        """
        return f"{self.title} by {self.author}"