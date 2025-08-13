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
from django.contrib.auth.models import User


# Views

## Login
from .auth.login import LoginAPI

### WhatsApp Variables
from .view.WhatsappVars import get_whatsapp_variables, create_whatsapp_variables, update_whatsapp_variables, delete_whatsapp_variables

## Contatos
from .view.Contatos import get_contacts, contact_create, contact_update, contact_delete

## Mensagens
from .view.Mensagens import get_messages, message_create, message_update, message_delete

## Kanban


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

