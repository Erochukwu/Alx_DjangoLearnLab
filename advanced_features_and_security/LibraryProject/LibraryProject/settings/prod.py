from .base import *

# SECURITY CONFIGURATIONS

# Set DEBUG to False in production to prevent detailed error pages from being shown
DEBUG = False
ALLOWED_HOSTS = ["yourdomain.com", "www.yourdomain.com"]

# Security headers
# Prevent MIME type sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True
# Prevent MIME type sniffing
SECURE_BROWSER_XSS_FILTER = True
# Prevent MIME type sniffing
X_FRAME_OPTIONS = "DENY"

# Secure cookies
# Ensure cookies are only sent over HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# HSTS
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Force HTTPS
SECURE_SSL_REDIRECT = True

# CSRF protection
CSRF_TRUSTED_ORIGINS = [
    "https://yourdomain.com",
    "https://www.yourdomain.com",
]
