from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import render
from .models import UserProfile

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome, Librarian! This view is restricted to Librarian users.")

def librarian_view(request):
    profiles = UserProfile.objects.all()
    return render(request, "relationship_app/librarian_view.html", {"profiles": profiles})
