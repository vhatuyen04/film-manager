from .models import Admin
from django.contrib.auth.backends import BaseBackend

class CustomBackend(BaseBackend):
    def authenticate(request, username=None, password=None):
        # Your custom authentication logic here
        # For example, check credentials against a different model
        try:
            user = Admin.objects.get(username=username)
            if user.check_password(password):
                return user
            else:
                return None
        except Admin.DoesNotExist:
            return None
        
def is_admin_user (user):
    # Authenticate the user

    # Check if the user is authenticated and is an admin
    if user is not None:  # Check if user is admin
        return True
    else:
        return False