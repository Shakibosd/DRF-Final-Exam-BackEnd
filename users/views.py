from .models import Profile
from rest_framework.authtoken.models import Token
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer, RegistrationSerializer, LoginSerializer
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

#user dekar jonno
class UserAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            user = get_object_or_404(User, pk=pk)
            serializer = UserSerializer(user) 
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        profile = get_object_or_404(Profile, user=user)

        user_serializer = UserSerializer(user, data=request.data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()

        profile_data = request.data.get('profile', {})
        profile.profile_img = profile_data.get('profile_img', profile.profile_img)
        profile.save()

        return Response(user_serializer.data)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  

#user register korar jonno
class RegisterAPIView(APIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            token = default_token_generator.make_token(user)
            print(token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("uid : ",uid)
            confirm_link = f'https://flower-seal-backend.vercel.app/users/active/{uid}/{token}/'
            print(confirm_link)
            email_subject = 'Confirm Your Email'
            email_body = render_to_string('confirm_email.html', {'confirm_link': confirm_link})
            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()
            return Response({'detail': 'Check your email for confirmation'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)

    except (User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('https://flower-seal.netlify.app/login.html')
    else:
        return redirect('https://flower-seal.netlify.app/register.html') 

#user login korar jonno
class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)

            if user:
                token, _ = Token.objects.get_or_create(user=user)
        
                login(request, user)
                return Response({'token': token.key, 'user_id': user.id}, status=status.HTTP_200_OK)
            
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

#user logout korar jonno
class LogoutAPIView(APIView):
    def get(self, request):
        user = request.user
        if hasattr(user, 'auth_token'):
            user.auth_token.delete()
        
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)