#Django settings for LibraryProject project.
#This file includes additional security configurations to enforce HTTPS,
#secure cookies, and protection headers against common attacks.

import os
from pathlib import Path

# Base directory path
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-37#yx!3tz8qm2gg6q3iuo^g54azorch1b^60xvrmkf@ke#1cg_"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Set False in production

ALLOWED_HOSTS = ["*"]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Local apps
    "bookshelf",
    "relationship_app",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",   # Required for many security settings    
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",   # Protects against CSRF attacks
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",    # Prevents clickjacking
]

ROOT_URLCONF = "LibraryProject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "LibraryProject.wsgi.application"

# ------------------------------------------------------------------------------
# Database (SQLite for local, replace with PostgreSQL/MySQL in production)
# ------------------------------------------------------------------------------    
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Custom user model
AUTH_USER_MODEL = "bookshelf.CustomUser"

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ----------------------------------------
# Security settings
# ----------------------------------------

# Enables the browser's built-in XSS (Cross-Site Scripting) protection
SECURE_BROWSER_XSS_FILTER = True

# Prevents the site from being displayed inside an iframe
# (protects against clickjacking attacks)
X_FRAME_OPTIONS = "DENY"

# Prevents the browser from trying to guess the content type (MIME sniffing)
# which helps reduce XSS attacks
SECURE_CONTENT_TYPE_NOSNIFF = True

# Ensures the CSRF cookie is only sent over HTTPS connections
# (set to False in local development if not using HTTPS)
CSRF_COOKIE_SECURE = True

# Ensures the session cookie is only sent over HTTPS connections
# (set to False in local development if not using HTTPS)
SESSION_COOKIE_SECURE = True

# ------------------------------------------------------------------------------
# HTTPS enforcement
# ------------------------------------------------------------------------------

# Redirect all non-HTTPS requests to HTTPS
# This ensures that communication between client and server is always encrypted.
SECURE_SSL_REDIRECT = True

