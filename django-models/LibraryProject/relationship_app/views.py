from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

def list_books_function_view(request):
    """Function-based view: lists all books with their authors"""
    books = Book.objects.all()
    response_text = "<h1>Books List (Function-Based View)</h1><ul>"
    for book in books:
        response_text += f"<li>{book.title} by {book.author.name}</li>"
    response_text += "</ul>"
    return HttpResponse(response_text)

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add all books in the library to the context
        context["books"] = self.object.books.all()
        return context


