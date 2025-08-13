from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from knox.views import LoginView as KnoxLoginView
from rest_framework import permissions
from django.contrib.auth import authenticate
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework import status

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