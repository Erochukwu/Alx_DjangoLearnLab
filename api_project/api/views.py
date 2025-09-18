from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.permissions import SAFE_METHODS, BasePermission

from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    """
    API endpoint that allows books to be viewed.

    Purpose:
        - Handles GET requests to retrieve a list of all Book records.
        - Uses the BookSerializer to convert model instances to JSON.
    
    Attributes:
        queryset (QuerySet): All Book objects in the database.
        serializer_class (Serializer): The serializer used to convert data.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for performing all CRUD operations on Book objects.

    Purpose:
        - Consolidates common actions for the Book model into one class.
        - Handles the following HTTP methods automatically:
            - GET (list & retrieve): Fetch all books or a single book.
            - POST (create): Add a new book.
            - PUT/PATCH (update): Modify an existing book.
            - DELETE (destroy): Remove a book.

    Attributes:
        queryset (QuerySet): All Book objects in the database.
        serializer_class (Serializer): The serializer used to convert data.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Apply permission rules
    permission_classes = [IsAuthenticated]  # Default: must be logged in

    class IsAdminOrReadOnly(BasePermission):
    # Custom permission:
    # ... SAFE_METHODS (GET, HEAD, OPTIONS) are allowed for any authenticated user...
    # - POST, PUT, PATCH, DELETE are restricted to admin users only."""
        def has_permission(self, request, view):
            if request.method in SAFE_METHODS:
                return request.user and request.user.is_authenticated
            return request.user and request.user.is_staff


