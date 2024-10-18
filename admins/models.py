from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    is_disabled = models.BooleanField(default=False)