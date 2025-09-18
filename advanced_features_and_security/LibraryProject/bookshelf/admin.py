from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Book

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Show these fields in the list view
    list_display = ["username", "email", "date_of_birth", "is_staff", "is_superuser"]

    # Allow filtering
    list_filter = ["is_staff", "is_superuser", "is_active"]

    # Add fields to the user detail page
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )

    # Add fields when creating a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )

# ✅ Register your model with admin
admin.site.register(CustomUser, CustomUserAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title',)

admin.site.register(Book, BookAdmin)