from django.db import models
from django.conf import settings
from django.db.models.query_utils import select_related_descend


User = settings.AUTH_USER_MODEL

class Platform(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name
    
    