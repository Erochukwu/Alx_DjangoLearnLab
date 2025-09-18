from rest_framework import generics
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

