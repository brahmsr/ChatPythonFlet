from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import *
from .serializers import *
import json

# Create your views here.

### Contact List View
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def contact_list(request, name=None):
    # retorna todos os contatos
    if request.method == 'GET':
        contacts = Contact.objects.all()
        
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)
        
    # retorna um contato específico
    elif request.method == 'GET' and name:
        try:
            contact = Contact.objects.get(pk=name)
            serializer = ContactSerializer(contact)
            return Response(serializer.data)
        except Contact.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    # cria um novo contato
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

### Message List View
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def message_list(request):
    if request.method == 'GET':
        messages = Message.objects.all()
        
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

### Contact Kanban List View
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def contact_kanban_list(request):
    if request.method == 'GET':
        kanbans = ContactKanban.objects.all()
        
        serializer = ContactKanbanSerializer(kanbans, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = ContactKanbanSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)
