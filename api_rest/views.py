from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import *
from .serializers import *
import json
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

# Create your views here.

## Contatos
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def contact_list(request, id: str):
    # retorna todos os contatos
    if request.method == 'GET':
        contacts = Contact.objects.all()
        
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    # retorna um contato específico
    elif id != None:
        if request.method == 'GET':
            try:
                contact = Contact.objects.get(id=id)
            except Contact.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ContactSerializer(contact)
            return Response(serializer.data)
        
    # atualiza um contato
    elif request.method == 'PUT':
        try:
            contact = Contact.objects.get(id=id)
        except Contact.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = json.loads(request.body)
        serializer = ContactSerializer(contact, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # deleta um contato
    elif request.method == 'DELETE':
        try:
            contact = Contact.objects.get(id=id)
        except Contact.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    # cria um novo contato
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


## Mensagens
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

## Kanban
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

## Login
@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # Gera ou recupera o token do usuário
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'username': user.username}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

## Logout
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    if request.method == 'POST':

        # Remove o token do usuário
        request.user.auth_token.delete()

        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
