from rest_framework import serializers
from .models import Contact, Message, ContactKanban, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        ordering = ['-timestamp']
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        ordering = ['-timestamp']
        fields = '__all__'

class ContactKanbanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactKanban
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']