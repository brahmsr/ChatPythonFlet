from django.db import models
from models import Enterprise

class SessionWhatsApp(models.Model):
    id = models.AutoField(primary_key=True)
    session_name = models.CharField(max_length=150, default='', db_index=True)
    session_data = models.TextField(default='', db_index=True)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, related_name='whatsapp_sessions')