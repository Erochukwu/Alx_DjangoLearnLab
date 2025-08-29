**Create a Book instance**

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
# <Book: Book object (1)>
```
*Book instance created successfully.*