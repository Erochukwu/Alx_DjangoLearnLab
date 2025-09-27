# API App (Django REST Framework)

This app exposes REST API endpoints for managing **Authors** and **Books**.

---

## Endpoints

### Index
- **GET** `/api/`
- Returns a welcome message.

---

### Books
- **GET** `/api/books/` → List all books (supports filters, search, ordering).
- **GET** `/api/books/<id>/` → Retrieve a single book.
- **POST** `/api/books/create/` → Create a new book (requires authentication).
- **PUT** `/api/books/<id>/update/` → Update a book (requires authentication).
- **DELETE** `/api/books/<id>/delete/` → Delete a book (requires authentication).

#### Custom Behavior:
- `publication_year` is validated to ensure it’s not in the future.
- Filtering: `?publication_year=YYYY` or `?author=<id>`
- Searching: `?search=keyword` (searches title and author name).
- Ordering: `?ordering=title` or `?ordering=publication_year`.

---

### Authors
- **GET** `/api/authors/` → List all authors.
- **GET** `/api/authors/<id>/` → Retrieve a single author (includes nested list of their books).

---

## Permissions
- **List & Detail (Books/Authors):** Public access.
- **Create, Update, Delete (Books):** Authenticated users only.

### Filtering & Search

The API supports flexible filtering for books.

#### Examples:
- List all books by a specific author:
GET /api/books/?author=2

- Filter by publication year:
GET /api/books/?publication_year=2021

- Filter by exact title:
GET /api/books/?title=The Hobbit

- Search across title and author name:
GET /api/books/?search=tolkien

- Order results by publication year (ascending/descending):
GET /api/books/?ordering=publication_year
GET /api/books/?ordering=-publication_year

### 🔎 Search Functionality

The API supports **text-based search** across the `title` and `author` fields.

#### Examples
- Search for books with "Hobbit" in the title:
GET /api/books/?search=Hobbit

- Search for books by author "Tolkien":
GET /api/books/?search=tolkien

- Search across both title and author:
GET /api/books/?search=ring

### 📑 Ordering

You can order book results by `title` or `publication_year`.

#### Examples
- Order alphabetically by title:
GET /api/books/?ordering=title

- Order by newest publication year first:
GET /api/books/?ordering=-publication_year

#### API Testing Documentation
### Testing Strategy

# The testing approach for this project focuses on verifying that the Book API endpoints work as expected, covering:

* CRUD Operations

- Listing all books (/api/books/)

- Retrieving a single book (/api/books/<id>/)

- Creating a new book (/api/books/create/)

- Updating a book (/api/books/<id>/update/)

- Deleting a book (/api/books/<id>/delete/)

- Filtering, Searching, and Ordering

- Filter by publication_year → /api/books/?publication_year=2020

- Filter by author → /api/books/?author=1

* Search by title/author → /api/books/?search=Hobbit

- Order by title or year → /api/books/?ordering=title or /api/books/?ordering=-publication_year

* Permissions & Authentication

- Anonymous users can list and retrieve books.

- Authenticated users can create and update.

- Only admin users can delete.

- Invalid or missing tokens return 401 Unauthorized.

* Validation

- Ensures that a book cannot be created/updated with a future publication_year.

#### Test Cases

- test_create_book_authenticated → verifies authenticated users can add a book.

- test_delete_book_admin_only → ensures only admins can delete books.

- test_search_books_by_title → checks that keyword searches return correct results.

- test_cannot_create_book_with_future_year → validates year constraints.

### Running Tests

* From the project root directory (advanced-api-project), run:
- python manage.py test api
This will:

Create a temporary test database.

Run all tests in api/test_views.py.

Tear down the test database when finished.

### Interpreting Results

- OK → All tests passed, API behaves correctly.

-  FAIL → Some tests failed. The console will show which test, the expected status code/data, and what was actually returned.

- ⚠️ ERROR → A configuration or runtime issue occurred (e.g., missing migrations or broken imports).

