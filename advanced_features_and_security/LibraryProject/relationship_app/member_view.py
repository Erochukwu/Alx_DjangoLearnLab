from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome, Member! This view is restricted to Member users.")