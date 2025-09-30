# blog/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views  # Django’s built-in authentication views
from . import views  # our custom views

urlpatterns = [
    # -------------------------
    # Blog routes
    # -------------------------
    path('', views.home, name='home'),   # Homepage → blog/views.home
    path('posts/', views.post_list, name='posts'),  # Blog posts → blog/views.post_list

    # -------------------------
    # Authentication routes
    # -------------------------
    # Built-in login view, customized to use our template blog/login.html
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),

    # Built-in logout view, customized to use blog/logout.html
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Custom registration view → blog/views.register
    path('register/', views.register, name='register'),

    # User profile route (custom view in blog/views.py)
    path('profile/', views.profile, name='profile'),
]

