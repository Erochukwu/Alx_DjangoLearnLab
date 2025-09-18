from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import BookList, BookViewSet

# Create a router instance
# The router will automatically generate routes for the BookViewSet
router = DefaultRouter()

# Register the BookViewSet with the router
# This will generate endpoints like:
#   /books_all/           (GET, POST)
#   /books_all/{id}/      (GET, PUT, PATCH, DELETE)
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (ListAPIView - read-only list of books)
    path('books/', BookList.as_view(), name='book-list'),

     # Token Authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    # Include all routes created by the router
    # These cover all CRUD operations for the BookViewSet
    path('', include(router.urls)),
]
