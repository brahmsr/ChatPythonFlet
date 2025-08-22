from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from ..Model import Message
from ..serializers import MessageSerializer
from rest_framework.response import Response
from rest_framework import status
import json

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_messages(request, id: str):
    if request.method == 'GET':
        try:
            messages = Message.Message.objects.all()
            
            serializer = MessageSerializer(messages, many=True)
            return Response(serializer.data)
        except Message.Message.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif id is not None:
        if request.method == 'GET':
            try:
                message = Message.Message.objects.get(id=id)
            except Message.Message.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = MessageSerializer(message)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def message_create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def message_update(request, id: str):
    if request.method == 'PUT':
        try:
            message = Message.Message.objects.get(id=id)
        except Message.Message.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = json.loads(request.body)
        serializer = MessageSerializer(message, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def message_delete(request, id: str):
    if request.method == 'DELETE':
        try:
            message = Message.Message.objects.get(id=id)
        except Message.Message.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
