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
from knox.views import LoginView as KnoxLoginView
from rest_framework import permissions
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

# Create your views here.

## Contatos
@api_view(['GET', 'POST', 'DELETE'])
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

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def contact_update(request, id: str):    
    # atualiza um contato
    if request.method == 'PUT':
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

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def contact_delete(request, id: str):
    # deleta um contato
    if request.method == 'DELETE':
        try:
            contact = Contact.objects.get(id=id)
        except Contact.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def contact_create(request):
    if request.method == 'POST':
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

## Dashboard
@api_view(['GET'])
def dashboard_stats(request):
    stats = {
        'total_users': User.objects.count(),
        'total_contacts': Contact.objects.count(),
        'total_messages': Message.objects.count(),
        'total_kanbans': ContactKanban.objects.count()
    }
    return Response(stats)

@api_view(['GET'])
def dashboard_users(request):
    users = User.objects.all().values('id', 'username', 'email', 'date_joined')
    return Response(list(users))

## Login
@method_decorator(csrf_exempt, name='dispatch')
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, format=None):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return super().post(request, format=None)
        return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
