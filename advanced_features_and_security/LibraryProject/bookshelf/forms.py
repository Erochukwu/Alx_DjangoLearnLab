from django import forms
from .models import Book

# Example form (checker requirement)
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

# A ModelForm for Book model (useful for add/edit book)
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]
