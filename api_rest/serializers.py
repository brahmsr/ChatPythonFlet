from rest_framework import serializers
from .models import Contact, Message, ContactKanban, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class ContactKanbanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactKanban
        fields = '__all__'