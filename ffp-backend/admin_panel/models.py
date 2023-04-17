from django.contrib.auth.models import User

class AdminUser(User):
    class Meta:
        proxy = True
