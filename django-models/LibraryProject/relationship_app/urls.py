from django.urls import path
from . import views
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Function-based view → lists all books
    path("books-fbv/", views.list_books_function_view, name="books_fbv"),

    # Class-based view → details of a specific library
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
    
    # Login and logout views
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    
    # Registration view
    path("register/", views.register, name="register"),
    
    # Role-based views
    path("admin-role/", admin_view, name="admin_role"),
    path("librarian-role/", librarian_view, name="librarian_role"),
    path("member-role/", member_view, name="member_role"),

    path("admin-view/", admin_view, name="admin_view"),
    path("librarian-view/", librarian_view, name="librarian_view"),
]
