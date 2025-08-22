from rest_framework import serializers
from .Model.Contact import Contact
from .Model.Message import Message
from .Model.KanbanContact import ContactKanban
from .Model.Profile import Profile
from .Model.Enterprise import Enterprise
from .Model.SessionWhatsapp import SessionWhatsApp
from .Model.WhatsappVariables import WhatsappVariables
from django.contrib.auth.models import User

## User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

## Contacts
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        ordering = ['-timestamp']
        fields = '__all__'

## Messages
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        ordering = ['-timestamp']
        fields = '__all__'

## Contact Kanban
class ContactKanbanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactKanban
        fields = '__all__'

## Login
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

## Whatsapp Variables
class WhatsappVariablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatsappVariables
        fields = '__all__'

class WhatsappVariablesEdit(serializers.ModelSerializer):
    class Meta:
        model = WhatsappVariables
        fields = ['name', 'value']