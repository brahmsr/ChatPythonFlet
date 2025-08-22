from django.db import models
from .Enterprise import Enterprise

class WhatsappVariables(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, default='', db_index=True)
    value = models.TextField(default='', db_index=True)
    enterprise = models.ManyToManyField(Enterprise, related_name='whatsapp_variables')

    def __str__(self):
        return f'Variable: {self.name} - {self.value}'