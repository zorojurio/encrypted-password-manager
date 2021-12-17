from django.db import models
from django.conf import settings
from django.db.models.query_utils import select_related_descend
from django.urls import reverse

User = settings.AUTH_USER_MODEL


class Platform(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('platforms:detail', kwargs={'pk': self.pk})

    def get_absolute_update_url(self):
        return reverse('platforms:update', kwargs={'pk': self.pk})

    def get_absolute_delete_url(self):
        return reverse('platforms:delete', kwargs={'pk': self.pk})
