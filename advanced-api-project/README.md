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
