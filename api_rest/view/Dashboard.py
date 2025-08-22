from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from ..Model import Message, Contact, KanbanContact
from rest_framework.response import Response
from django.contrib.auth.models import User

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_stats(request):
    stats = {
        'total_users': User.objects.count(),
        'total_contacts': Contact.Contact.objects.count(),
        'total_messages': Message.Message.objects.count(),
        'total_kanbans': KanbanContact.ContactKanban.objects.count()
    }
    return Response(stats)

@api_view(['GET'])
def dashboard_users(request):
    users = User.objects.all().values('id', 'username', 'email', 'date_joined')
    return Response(list(users))