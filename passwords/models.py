from django.db import models
from django.conf import settings
from platforms.models import Platform

User = settings.AUTH_USER_MODEL
class PlatformPassword(models.Model):
    password = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.user.username
    
    
    