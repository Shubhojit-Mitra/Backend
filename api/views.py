from django.contrib.auth import authenticate, login, logout
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer

class RegisterView(views.APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            response = Response({"message": "Registered successfully."}, status=status.HTTP_201_CREATED)
            response.set_cookie(
                key='auth_token',
                value=token.key,
                httponly=True,
                samesite='Lax'  # Adjust according to your cross-site request needs
            )
            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(views.APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            response = Response({"message": "Logged in successfully."}, status=status.HTTP_200_OK)
            response.set_cookie(
                key='auth_token',
                value=token.key,
                httponly=True,
                samesite='Lax'  # Adjust according to your cross-site request needs
            )
            return response
        else:
            return Response({"message": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(views.APIView):
    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        response = Response({"message": "Successfully logged out."})
        response.delete_cookie('auth_token')

        return response

class HelloView(views.APIView):
    def get(self, request):
        print(request.user)
        if request.user.is_authenticated:
            return Response({"message": f"Hello, {request.user.username}!"})
        return Response({"message": "Hello, world!"})