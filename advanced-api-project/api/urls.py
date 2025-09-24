from django.http import JsonResponse
from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

def index(request):
    return JsonResponse({"message": "Welcome to the API"})

"""
URL Configuration for the API app
---------------------------------
This module maps URL routes to the corresponding generic views for the Book model.
Each endpoint is designed to handle a specific CRUD operation.

Endpoints:
    - /books/                → List all books (GET)
    - /books/<int:pk>/       → Retrieve a single book by ID (GET)
    - /books/create/         → Create a new book (POST)
    - /books/<int:pk>/update/ → Update an existing book (PUT/PATCH)
    - /books/<int:pk>/delete/ → Delete an existing book (DELETE)
"""

urlpatterns = [
    path('', BookListView.as_view(), name='api_index'),  # <-- If you want an index
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]

