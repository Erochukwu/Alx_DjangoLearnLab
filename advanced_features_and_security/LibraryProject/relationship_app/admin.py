from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from bookshelf.models import CustomUser
from .models import UserProfile, Author, Library, Librarian

# Register other models
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role")


admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Librarian)
