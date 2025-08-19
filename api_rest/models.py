
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

from Model.Profile import Profile
from Model.Enterprise import Enterprise
from Model.Contact import Contact
from Model.Message import Message
from Model.KanbanContact import ContactKanban
from Model.WhatsappVariables import WhatsappVariables

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Cria o perfil com valores padrões para campos que não existem no User
        Profile.objects.create(
            user=instance,
            name=instance.first_name or "Nome",
            lastname=instance.last_name or "Sobrenome",
            phone="449999-9999",  # padrão
            avatar=None,  # padrão
            enterprise=None  # padrão
        )
    else:
        # Atualiza ou cria o perfil se não existir
        Profile.objects.update_or_create(
            user=instance,
            defaults={
                "name": instance.first_name or "Nome",
                "lastname": instance.last_name or "Sobrenome",
                "phone": "449999-9999",  # mantém padrão
                "avatar": None,
                "enterprise": None
            }
        )
    
    
