from django.urls import path
from .views import list_books_function_view, LibraryDetailView

urlpatterns = [
    # Function-based view → lists all books
    path("books-fbv/", list_books_function_view, name="books_function_view"),

    # Class-based view → details of a specific library
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
]