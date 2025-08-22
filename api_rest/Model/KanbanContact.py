from django.db import models
from .Contact import Contact
from ..models import User

class ContactKanban(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    ]
    
    id = models.AutoField(primary_key=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    responsible = models.ManyToManyField(User, related_name='kanban_contacts')
    labels = models.CharField(max_length=150, default='', db_index=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='todo')
    
    def __str__(self):
        return f'Kanban: {self.contact.name} - {self.get_status_display()}'