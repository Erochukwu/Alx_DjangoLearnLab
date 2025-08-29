**Delete the Book instance**

```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(Book.objects.all())
# <QuerySet []>
```
*Book instance deleted successfully.*