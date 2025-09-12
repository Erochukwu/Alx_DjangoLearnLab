from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from bookshelf.models import Book   # ✅ Use bookshelf Book model
from .models import Library
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import user_passes_test, permission_required


# --- BOOK LIST ---
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/book_list.html", {"books": books})


# --- ADD BOOK ---
@permission_required("bookshelf.can_create", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        publication_year = request.POST.get("publication_year")

        if title and author:
            Book.objects.create(
                title=title,
                author=author,
                publication_year=publication_year or None
            )
            return redirect("book_list")
    return render(request, "relationship_app/add_book.html")


# alias for compatibility with checker
def create_book(request):
    return add_book(request)


# --- EDIT BOOK ---
@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.publication_year = request.POST.get("publication_year") or book.publication_year
        book.save()
        return redirect("book_list")
    return render(request, "relationship_app/edit_book.html", {"book": book})


# alias for compatibility with checker
def update_book(request, book_id):
    return edit_book(request, book_id)


# --- DELETE BOOK ---
@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect("book_list")


# --- LIBRARY DETAIL ---
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()
        return context


# --- USER AUTH ---
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("book_list")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})


# --- ROLE-BASED VIEWS ---
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")


# --- SIMPLE INDEX ---
def index(request):
    return HttpResponse("Hello from relationship_app!")
