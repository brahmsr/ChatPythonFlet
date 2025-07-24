from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, default='', db_index=True)
    telephone = models.CharField(max_length=20, unique=True, db_index=True, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Contact: {self.name} with {self.telephone}'
    
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Contact, on_delete=models.CASCADE, default='')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.content} - Message from {self.user.name} ({self.user.telephone}) at {self.timestamp}'
    
class ContactKanban(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Contact, on_delete=models.CASCADE, default='')
    responsible = models.ForeignKey(User, on_delete=models.CASCADE)
    labels = models.CharField(max_length=150, default='', db_index=True)
    status = models.enums.TextChoices('To Do', 'Doing', 'Done')
