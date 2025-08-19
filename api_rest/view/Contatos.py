from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from ..Model import Contact
from rest_framework.response import Response
import json
from ..serializers import ContactSerializer
from rest_framework import status

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_contacts(request, id: str):
    # retorna todos os contatos
    if request.method == 'GET':
        contacts = Contact.Contact.objects.all()
        
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    # retorna um contato específico
    elif id != None:
        if request.method == 'GET':
            try:
                contact = Contact.Contact.objects.get(id=id)
            except Contact.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ContactSerializer(contact)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def contact_update(request, id: str):    
    # atualiza um contato
    if request.method == 'PUT':
        try:
            contact = Contact.Contact.objects.get(id=id)

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
            contact = Contact.Contact.objects.get(id=id)
        except Contact.Contact.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
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
