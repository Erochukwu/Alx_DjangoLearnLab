from rest_framework import serializers
from .models import Author, Book
from datetime import date

"""
Serializers: AuthorSerializer and BookSerializer

Serializers allow converting Django model instances into JSON (for APIs)
and validating JSON input into Python objects before saving to the database.

We define:
    - BookSerializer: Handles serialization and validation for Book objects.
    - AuthorSerializer: Handles serialization for Author objects,
      including a nested representation of related Book objects.

Relationship in serialization:
    - BookSerializer serializes each Book independently.
    - AuthorSerializer nests BookSerializer to show all related books
      whenever an Author is serialized.
"""


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.

    Responsibilities:
        - Serializes all fields of the Book model (id, title, publication_year, author).
        - Ensures publication_year cannot be set to a future year (custom validation).
    """

    class Meta:
        model = Book
        fields = "__all__"

    def validate_publication_year(self, value: int) -> int:
        """
        Custom field-level validation for publication_year.

        Args:
            value (int): The provided year for publication.

        Returns:
            int: The validated publication year.

        Raises:
            serializers.ValidationError: If the year is greater than the current year.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future. Current year is {current_year}."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.

    Responsibilities:
        - Serializes Author fields (id, name).
        - Dynamically includes related books using BookSerializer.
          This creates a nested structure so that when fetching an Author,
          you also see all their Books inline.
    """

    # Nesting BookSerializer to represent related books
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books"]
