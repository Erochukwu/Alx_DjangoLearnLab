# blog/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    # -------------------------
    # Blog Post URLs
    # -------------------------

    # Homepage showing all posts
    path('', PostListView.as_view(), name='home'),

    # Post list (tests/templates expect 'post_list')
    path('posts/', PostListView.as_view(), name='post_list'),

    # Alias for legacy tests/templates: 'posts'
    path('posts/', PostListView.as_view(), name='posts'),

    # Post detail view
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    # Create a new post (login required)
    path('post/new/', PostCreateView.as_view(), name='post_create'),

    # Update post (author only)
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),

    # Delete post (author only)
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    # -------------------------
    # Authentication URLs
    # -------------------------

    # Login
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),

    # Logout
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Register
    path('register/', views.register, name='register'),

    # Profile
    path('profile/', views.profile, name='profile'),
]
