from django.urls import path
from django.contrib.auth import views as auth_views

from . import views  # keep this for register & profile
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView, PostsByTagListView, PostSearchListView,
    CommentCreateView, CommentUpdateView, CommentDeleteView
)

urlpatterns = [
    # -------------------------
    # Blog Post URLs
    # -------------------------

    # Homepage showing all posts
    path('', PostListView.as_view(), name='home'),

    # Post list
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/', PostListView.as_view(), name='posts'),

    # Tag and search url
    path("tags/<str:tag_name>/", PostsByTagListView.as_view(), name="posts_by_tag"),
    path("search/", PostSearchListView.as_view(), name="post_search"),


    # Post detail view
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    # Create a new post (login required)
    path('post/new/', PostCreateView.as_view(), name='post_create'),

    # Update post (author only)
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),

    # Delete post (author only)
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    # -------------------------
    # Comment URLs (Class-Based Views)
    # -------------------------
    # Create a new comment on a post
path(
    "post/<int:pk>/comments/new/",
    CommentCreateView.as_view(),
    name="comment_create"
),

# Edit a specific comment (author only)
path(
    "comment/<int:pk>/update/",
    CommentUpdateView.as_view(),
    name="comment_update"
),

# Delete a specific comment (author only)
path(
    "comment/<int:pk>/delete/",
    CommentDeleteView.as_view(),
    name="comment_delete"
),


    # -------------------------
    # Authentication URLs
    # -------------------------
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Register & Profile
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
