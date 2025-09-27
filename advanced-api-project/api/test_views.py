from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from .models import Book, Author
from datetime import date


class BookAPITests(APITestCase):
    """
    Book API Test Suite
    -------------------
    Covers:
      - CRUD operations
      - Filtering, searching, and ordering
      - Permissions and authentication
      - Data validation (publication_year rules)
    """

    def setUp(self):
        # Create test users
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.admin = User.objects.create_superuser(username="admin", password="adminpass")

        # Tokens for authentication
        self.user_token = Token.objects.create(user=self.user)
        self.admin_token = Token.objects.create(user=self.admin)

        # Authenticate default client as normal user
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.user_token.key}")

        # Create author and books
        self.author = Author.objects.create(name="J.R.R. Tolkien")
        self.book1 = Book.objects.create(title="The Hobbit", author=self.author, publication_year=1937)
        self.book2 = Book.objects.create(title="The Lord of the Rings", author=self.author, publication_year=1954)
        self.book3 = Book.objects.create(title="Silmarillion", author=self.author, publication_year=1977)

    # -----------------
    # CRUD Tests
    # -----------------

    def test_list_books(self):
        """Test listing all books (open to everyone)."""
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 3)

    def test_retrieve_book(self):
        """Test retrieving a single book by ID."""
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "The Hobbit")

    def test_create_book_authenticated(self):
        """Test creating a book (authenticated user only)."""
        url = reverse("book-create")
        data = {"title": "New Book", "author": self.author.id, "publication_year": 2020}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book_authenticated(self):
        """Test updating a book (authenticated user only)."""
        url = reverse("book-update", args=[self.book1.id])
        data = {"title": "Updated Title", "author": self.author.id, "publication_year": 1937}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Title")

    def test_delete_book_admin_only(self):
        """Test deleting a book (admin required)."""
        url = reverse("book-delete", args=[self.book1.id])

        # Normal user should not be allowed
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Switch to admin
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.admin_token.key}")
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # -----------------
    # Filtering, Searching, Ordering
    # -----------------

    def test_filter_books_by_publication_year(self):
        """Test filtering books by publication year."""
        url = reverse("book-list") + "?publication_year=1937"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(b["publication_year"] == 1937 for b in response.data))

    def test_filter_books_by_author(self):
        """Test filtering books by author ID."""
        url = reverse("book-list") + f"?author={self.author.id}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(b["author"] == self.author.id for b in response.data))

    def test_search_books_by_title(self):
        """Test searching books by title keyword."""
        url = reverse("book-list") + "?search=Hobbit"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Hobbit" in b["title"] for b in response.data))

    def test_order_books_by_title(self):
        """Test ordering books alphabetically by title."""
        url = reverse("book-list") + "?ordering=title"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [b["title"] for b in response.data]
        self.assertEqual(titles, sorted(titles))

    def test_order_books_by_publication_year_desc(self):
        """Test ordering books by publication year descending."""
        url = reverse("book-list") + "?ordering=-publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [b["publication_year"] for b in response.data]
        self.assertEqual(years, sorted(years, reverse=True))

    # -----------------
    # Validation
    # -----------------

    def test_cannot_create_book_with_future_year(self):
        """Test that creating a book with a future publication year fails."""
        url = reverse("book-create")
        future_year = date.today().year + 1
        data = {"title": "Future Book", "author": self.author.id, "publication_year": future_year}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Publication year cannot be in the future.", str(response.data))
