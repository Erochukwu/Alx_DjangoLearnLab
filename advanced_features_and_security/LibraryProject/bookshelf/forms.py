from django import forms
from .models import Book

# A ModelForm for creating/updating Book instances
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]  # include the fields you need
