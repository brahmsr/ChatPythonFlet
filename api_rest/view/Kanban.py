from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from ..models import ContactKanban
from ..serializers import ContactKanbanSerializer
from rest_framework.response import Response
from rest_framework import status
import json

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def contact_kanban_get(request):
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