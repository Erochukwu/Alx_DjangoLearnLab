from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  
    # Example: GET /api/books/ → returns a list of all books
]
