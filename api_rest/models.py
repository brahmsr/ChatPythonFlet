from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Enterprise(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default='', db_index=True)
    logo = models.ImageField(upload_to='enterprise_logos/', null=True, blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(null=False, blank=False)
    lastname = models.CharField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.SET_NULL, null=True, blank=True, related_name='employees')

    def __str__(self):
        return f'Perfil de {self.user.username}'

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            name=instance.first_name or "Nome",
            lastname=instance.last_name or "Sobrenome",
            phone=instance.phone or "",
            avatar=instance.avatar or "",
            enterprise=instance.enterprise or None
        )
    else:
        try:
            profile = instance.profile
            profile.name = instance.first_name or "Nome"
            profile.lastname = instance.last_name or ""
            profile.phone = instance.phone or ""
            profile.avatar = instance.avatar or ""
            profile.enterprise = instance.enterprise or None
            profile.save()
        except Profile.DoesNotExist:
            Profile.objects.create(
                user=instance,
                name=instance.first_name or "Nome",
                lastname=instance.last_name or "",
                phone=instance.phone or "",
                avatar=instance.avatar or "",
                enterprise=instance.enterprise or None
            )
    
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, default='', db_index=True)
    telephone = models.CharField(max_length=20, unique=True, db_index=True, blank=False, null=False, validators=[
        RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    ])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Contact: {self.name} with {self.telephone}'

### Message Model    
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.content} - Message from {self.contact.name} ({self.contact.telephone}) at {self.timestamp}'
    
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

class WhatsappVariables(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, default='', db_index=True)
    value = models.TextField(default='', db_index=True)
    enterprise = models.ManyToManyField(Enterprise, related_name='whatsapp_variables')

    def __str__(self):
        return f'Variable: {self.name} - {self.value}'