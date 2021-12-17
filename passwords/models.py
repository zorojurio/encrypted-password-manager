from django.db import models
from django.conf import settings
from django.urls import reverse
from platforms.models import Platform

User = settings.AUTH_USER_MODEL


class PlatformPassword(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('passwords:detail', kwargs={'pk': self.pk})
    
    def get_absolute_update_url(self):
        return reverse('passwords:update', kwargs={'pk': self.pk})
    
    def get_absolute_delete_url(self):
        return reverse('passwords:delete', kwargs={'pk': self.pk})