from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from ..models import Message, User, Contact, ContactKanban
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
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