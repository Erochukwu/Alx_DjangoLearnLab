from django.shortcuts import render
from .models import UserProfile

def admin_view(request):
    profiles = UserProfile.objects.all()
    return render(request, "relationship_app/admin_view.html", {"profiles": profiles})
