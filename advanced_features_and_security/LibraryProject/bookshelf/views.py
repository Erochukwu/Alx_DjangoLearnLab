# bookshelf/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

# View books (requires can_view)
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

# Create a new book (requires can_create)
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        year = request.POST.get("year")
        Book.objects.create(title=title, author=author, publication_year=year)
        return redirect("book_list")
    return render(request, "bookshelf/create_book.html")

# Edit an existing book (requires can_edit)
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.publication_year = request.POST.get("year")
        book.save()
        return redirect("book_list")
    return render(request, "bookshelf/edit_book.html", {"book": book})

# Delete a book (requires can_delete)
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "bookshelf/delete_book.html", {"book": book})

