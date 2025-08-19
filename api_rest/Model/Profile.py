from django.db import models
from django.contrib.auth.models import User
from .Enterprise import Enterprise

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=150, null=False, blank=False)
    lastname = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.SET_NULL, null=True, blank=True, related_name='employees')

    def __str__(self):
        return f'Perfil de {self.user.username}'
