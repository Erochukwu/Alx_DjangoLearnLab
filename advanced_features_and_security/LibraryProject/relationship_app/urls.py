from django.urls import path
from . import views

urlpatterns = [
    # Book management
    path("books/", views.list_books, name="book_list"),
    path("add_book/", views.add_book, name="add_book"),
    path("edit_book/<int:book_id>/", views.edit_book, name="edit_book"),
    path("delete_book/<int:book_id>/", views.delete_book, name="delete_book"),
    path("create_book/", views.create_book, name="create_book"),  # alias for checker
    path("update_book/<int:book_id>/", views.update_book, name="update_book"),  # alias for checker

    # Library details
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # Authentication
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.login, name="logout"),  # placeholder unless you add a logout view

    # Role-based views
    path("admin-role/", views.admin_view, name="admin_role"),
    path("librarian-role/", views.librarian_view, name="librarian_role"),
    path("member-role/", views.member_view, name="member_role"),

    # Index page
    path("", views.index, name="index"),
]

