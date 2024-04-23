from .models import User
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser
from .serializers import UserSerializer
from django.http import JsonResponse
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
import jwt, datetime

# class UserView(viewsets.ModelViewSet):
    # parser_classes = (MultiPartParser, FormParser)
    # serializer_class = UserSerializer
    # queryset = User.objects.all()

    # def post(self, request):
    #     data = request.data
    #     serializer = UserSerializer(data=data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse("User Added Successfully", safe=False)
    #     return JsonResponse("Failed to Add User", safe=False)

    # def put(self, request, id=None):
    #     book_to_update = User.objects.get(id=id)
    #     serializer = UserSerializer(
    #         instance=book_to_update, data=request.data, partial=True)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse("User updated Successfully", safe=False)
    #     return JsonResponse("Failed To Update User")
    # pass


class RegisterView(APIView):
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)

class LoginView(APIView):
    
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = User.objects.filter(email=email).first()
        
        if user is None:
            raise AuthenticationFailed("User is not found..")
        
        if not user.check_password(password):
            raise AuthenticationFailed("Password is incorrect")
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }

        return response
    
class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get("jwt")
        if not token:
            raise AuthenticationFailed("UnAuthenticated")
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("UnAuthenticated")
        
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)
    
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            "message": "logout seccussful"
        }

        return response