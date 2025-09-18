from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.

    Purpose:
        - Converts Book model instances into JSON so they can be returned in API responses.
        - Converts JSON data back into Book model instances for creating or updating records.

    Fields:
        All fields from the Book model (id, title, author) are included.
    """

    class Meta:
        model = Book
        # Include every field from the Book model automatically:
        # id (auto-generated), title, and author
        fields = "__all__"
