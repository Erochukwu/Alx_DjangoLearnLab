from django.contrib import admin
from .models import Author, Book

"""
Admin configuration for the Author and Book models.
This allows managing Authors and Books through the Django Admin interface.
"""

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Admin view for Author model.
    Displays the author's name and the count of their books.
    """
    list_display = ("id", "name", "book_count")

    def book_count(self, obj):
        """Show how many books this author has."""
        return obj.books.count()
    book_count.short_description = "Number of Books"


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Admin view for Book model.
    Displays title, publication year, and linked author.
    """
    list_display = ("id", "title", "publication_year", "author")
    list_filter = ("publication_year", "author")
    search_fields = ("title", "author__name")
