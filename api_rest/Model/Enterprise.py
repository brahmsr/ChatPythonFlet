from django.db import models

class Enterprise(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default='', db_index=True)
    logo = models.ImageField(upload_to='enterprise_logos/', null=True, blank=True)