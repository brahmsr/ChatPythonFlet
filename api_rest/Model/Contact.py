from django.db import models
from django.core.validators import RegexValidator

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, default='', db_index=True)
    telephone = models.CharField(max_length=20, unique=True, db_index=True, blank=False, null=False, validators=[
        RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    ])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Contact: {self.name} with {self.telephone}'