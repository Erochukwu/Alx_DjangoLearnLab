from relationship_app.models import Author, Book, Library, Librarian


def query_books_by_author(author_name):
    """Query all books by a specific author"""
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return []


def list_books_in_library(library_name):
    """List all books in a library"""
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []


def get_librarian_for_library(library_name):
    """Retrieve the librarian for a library"""
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian  # thanks to OneToOneField related_name="librarian"
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None


# Sample usage (for testing in Django shell or script execution)
if __name__ == "__main__":
    # Query all books by an author
    print("Books by 'George Orwell':")
    for book in query_books_by_author("George Orwell"):
        print(f"- {book.title}")

    # List all books in a library
    print("\nBooks in 'Central Library':")
    for book in list_books_in_library("Central Library"):
        print(f"- {book.title}")

    # Retrieve the librarian for a library
    librarian = get_librarian_for_library("Central Library")
    if librarian:
        print(f"\nLibrarian of Central Library: {librarian.name}")
    else:
        print("\nNo librarian found for Central Library.")
