from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from ..models import WhatsappVariables
from rest_framework.response import Response
import json
from ..serializers import WhatsappVariablesSerializer, WhatsappVariablesEdit
from rest_framework import status

### Obtenção das variáveis
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def whatsapp_variables_get(request, name):
    if request.method == 'GET':
        try:
            variables = WhatsappVariables.objects.get(name=name, user=request.user)
            if variables:
                serializer = WhatsappVariablesSerializer(variables)
                return Response(serializer.data)
            else:
                return Response({'error': 'Variables not found'}, status=404)
        
        except Exception as e:
            return Response({'error': str(e)}, status=400)

### Criação de variável    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_whatsapp_variables(request):

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            serializer = WhatsappVariablesSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({'error': str(e)}, status=400)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

### Edição das variáveis
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_whatsapp_variables(request, id: str):

    if request.method == 'PUT':
        variables = WhatsappVariables.objects.get(id=id, name=request.body['name'], user=request.user)
        if variables:
            try:
                data = json.loads(request.body)
                serializer = WhatsappVariablesEdit(instance=variables, data=data)

                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            except Exception as e:
                return Response({'error': str(e)}, status=400)
    
        else:
            return Response({'error': 'Variables not found'}, status=404)
    
### Deleção da variável
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_whatsapp_variables(request, id: str):
    # deleta uma variável
    if request.method == 'DELETE':
        try:
            variables = WhatsappVariables.objects.get(id=id, user=request.user)
        except WhatsappVariables.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        variables.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)