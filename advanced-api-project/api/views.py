from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, permissions, filters
from rest_framework.exceptions import ValidationError
from datetime import date
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

@api_view(['GET'])
def index(request):
    return Response({"message": "Welcome to the API (DRF enabled)"})



"""
Customized Generic Views for Book Model
---------------------------------------
We extend Django REST Framework's generic views and override certain methods
to provide extra validation, permission checks, and filtering options.
"""

class BookListView(generics.ListAPIView):
    """
    BookListView
    ------------
    Purpose:
        Retrieve a list of all books stored in the database.
        Supports filtering by publication_year and author.
    Features:
        - GET: Returns a JSON array of all books.
        - Filtering: Allows ?publication_year=YYYY or ?author=<author_id>.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]   # ✅ anyone can read
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "author__name"]
    ordering_fields = ["publication_year", "title"]

    def get_queryset(self):
        queryset = super().get_queryset()
        year = self.request.query_params.get("publication_year")
        author = self.request.query_params.get("author")

        if year:
            queryset = queryset.filter(publication_year=year)
        if author:
            queryset = queryset.filter(author__id=author)
        return queryset


class BookDetailView(generics.RetrieveAPIView):
    """Retrieve a single book by ID."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]   # ✅ anyone can read


class BookCreateView(generics.CreateAPIView):
    """
    BookCreateView
    --------------
    Purpose:
        Create a new book entry in the database.
    Customizations:
        - Requires authentication.
        - Validates publication_year against current year.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]   # ✅ auth required

    def perform_create(self, serializer):
        # Extra validation: publication_year must not be in the future
        if serializer.validated_data["publication_year"] > date.today().year:
            raise ValidationError("Publication year cannot be in the future.")
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    BookUpdateView
    --------------
    Purpose:
        Update an existing book record.
    Customizations:
        - Requires authentication.
        - Validates publication_year against current year.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]    # ✅ auth required

    def perform_update(self, serializer):
        # Extra validation: publication_year must not be in the future
        if serializer.validated_data.get("publication_year", date.today().year) > date.today().year:
            raise ValidationError("Publication year cannot be in the future.")
        serializer.save()

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Safe methods = GET, HEAD, OPTIONS (always allowed)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only admins for unsafe methods
        return request.user and request.user.is_staff

class BookDeleteView(generics.DestroyAPIView):
    """Delete an existing book record. Requires authentication."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]     # ✅ auth required   
