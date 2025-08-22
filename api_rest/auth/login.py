from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from knox.views import LoginView as KnoxLoginView
from rest_framework import permissions
from django.contrib.auth import authenticate
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework import status
from knox.models import AuthToken
from ..Model.Profile import Profile
from datetime import timedelta

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
            token = AuthToken.objects.create(user)[1]
            expiry_time = timedelta(hours=24)
            token_obj = AuthToken.objects.create(user, expiry=expiry_time)
            token = token_obj[1]
            expiry = token_obj[0].expiry
            
            profile_data = {}
            try:
                profile = user.profile
                profile_data = {
                    'name': profile.name,
                    'lastname': profile.lastname,
                    'phone': profile.phone,
                    'avatar': profile.avatar.url if profile.avatar else None,
                    'enterprise': profile.enterprise.name if profile.enterprise else None,
                    'enterprise_id': profile.enterprise.id if profile.enterprise else None
                }
            except Profile.DoesNotExist:
                pass
            
            return Response({
                'token': token,
                'expiry': expiry,
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'profile': profile_data
                }
            })
        
        return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)