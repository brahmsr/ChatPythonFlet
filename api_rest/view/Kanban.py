from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from ..Model import KanbanContact
from ..serializers import ContactKanbanSerializer
from rest_framework.response import Response
from rest_framework import status
import json

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def get_contact_kanban(request, id: str):
    
    # Get all kanbans
    if request.method == 'GET':
        kanbans = KanbanContact.ContactKanban.objects.all()
        
        serializer = ContactKanbanSerializer(kanbans, many=True)
        return Response(serializer.data)
    
    # Get a specific kanban by ID
    elif request.method == 'GET' and id is not None:
        try:
            kanban = KanbanContact.ContactKanban.objects.get(id=id)
        except KanbanContact.ContactKanban.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ContactKanbanSerializer(kanban)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_contact_kanban(request):
    if request.method == 'POST':
        serializer = ContactKanbanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_contact_kanban(request, id: str):
    if request.method == 'PUT':
        try:
            kanban = KanbanContact.ContactKanban.objects.get(id=id)
        except KanbanContact.ContactKanban.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ContactKanbanSerializer(kanban, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_contact_kanban(request, id: str):
    if request.method == 'DELETE':
        try:
            kanban = KanbanContact.ContactKanban.objects.get(id=id)
        except KanbanContact.ContactKanban.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        kanban.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)