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


