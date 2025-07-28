from rest_framework import serializers
from .models import Contact, Message, ContactKanban, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'telephone', 'timestamp']
        ordering = ['-timestamp']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'user.name', 'user.telephone', 'content', 'timestamp', 'read']
        ordering = ['-timestamp']

class ContactKanbanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactKanban
        fields = ['id', 'user.name', 'user.telephone']