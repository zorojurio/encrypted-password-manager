from Crypto.Cipher import AES
from django.conf import settings
from django.db import models
from masters.utils import encrypt_master_password

User = settings.AUTH_USER_MODEL


class MasterPassword(models.Model):
    password = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.password = encrypt_master_password(self.password)
        super(MasterPassword, self).save(*args, **kwargs)
