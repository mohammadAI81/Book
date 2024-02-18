from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomAdmin(AbstractUser):
    email = models.EmailField(blank=False, null=False)
    date_birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True)
    # photo
    # status
    
    def __str__(self):
        return self.username
    
    
