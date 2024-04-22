from .models import User
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from .serializers import UserSerializer
from django.http import JsonResponse

class UserView(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("User Added Successfully", safe=False)
        return JsonResponse("Failed to Add User", safe=False)

    def put(self, request, id=None):
        book_to_update = User.objects.get(id=id)
        serializer = UserSerializer(
            instance=book_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("User updated Successfully", safe=False)
        return JsonResponse("Failed To Update User")
