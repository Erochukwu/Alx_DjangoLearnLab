from django.db import models

"""
Models: Author and Book

This file defines the database structure for our API.
We have two models:
    - Author: Represents an author who can write many books.
    - Book: Represents a single book, linked to one author.

Relationship:
    - One-to-Many (Author → Books)
    - Implemented using a ForeignKey in Book pointing to Author.
    - When an Author is deleted, all their related Books are deleted too (on_delete=models.CASCADE).
"""


class Author(models.Model):
    """
    Represents an author.

    Fields:
        name (CharField): The name of the author.

    Relationships:
        - One Author can be linked to many Books through the Book model.
        - Reverse access: An author's books can be accessed via `author.books.all()`
          because of the `related_name="books"` in the Book model.
    """
    name = models.CharField(
        max_length=255,
        help_text="The full name of the author."
    )

    def __str__(self) -> str:
        """
        String representation of the Author object.
        Returns the author's name.
        """
        return self.name


class Book(models.Model):
    """
    Represents a book.

    Fields:
        title (CharField): The title of the book.
        publication_year (IntegerField): Year the book was published.
        author (ForeignKey): Link to the author who wrote the book.

    Relationships:
        - Each Book belongs to a single Author.
        - The `related_name="books"` allows us to fetch all books
          for an Author easily: `author.books.all()`.
    """
    title = models.CharField(
        max_length=255,
        help_text="The title of the book."
    )
    publication_year = models.IntegerField(
        help_text="The year this book was published."
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books",
        help_text="The author who wrote this book. Deleting the author will also delete their books."
    )

    def __str__(self) -> str:
        """
        String representation of the Book object.
        Returns the book title along with its publication year.
        """
        return f"{self.title} ({self.publication_year})"
