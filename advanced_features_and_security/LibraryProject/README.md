# Learning Django
# Library Project – Permissions and Groups Setup

## Custom Permissions
The `Book` model defines three custom permissions in `bookshelf/models.py`:

- `can_create` → Allows a user to create a new book.
- `can_edit` → Allows a user to edit an existing book.
- `can_delete` → Allows a user to delete a book.

These permissions are automatically created in the database after running migrations.

## Groups - we created three groups namely admin, Editors and Viewers
We created a group called **Admin** with the following permissions:
- `can_create`
- `can_delete`
- `can_edit`
- `can_view` (default Django view permission)

We created a group called **Editors** with the following permissions:
- `can_create`
- `can_edit`
- `can_view` (default Django view permission)

We created a group called **Viewers** with the following permissions:
- `can_view` (default Django view permission)

Example (in Django shell):

```python
from django.contrib.auth.models import Group, Permission
from bookshelf.models import Book

# Create group
editors = Group.objects.create(name="Editors")

# Assign permissions
perms = Permission.objects.filter(codename__in=["can_create", "can_edit", "can_view"])
editors.permissions.set(perms)
