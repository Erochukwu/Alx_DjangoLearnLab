from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books_function_view, LibraryDetailView, register

urlpatterns = [
    # Function-based view → lists all books
    path("books-fbv/", list_books_function_view, name="books_fbv"),

    # Class-based view → details of a specific library
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    
    # ...other patterns...
    path("login/", auth_views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", register, name="register"),
]