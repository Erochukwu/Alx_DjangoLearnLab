from django.shortcuts import render
from .models import Book


def list_books(request):
    """View to list all books"""
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

