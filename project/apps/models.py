from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_super_admin = models.BooleanField(default=False)  # Custom field to check if user is a super admin



