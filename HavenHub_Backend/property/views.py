from .models import Property
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from .serializers import PropertySerializer
from django.http import JsonResponse

class PropertyView(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = PropertySerializer
    queryset = Property.objects.all()

    def post(self, request):
        data = request.data
        serializer = PropertySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Property Added Successfully", safe=False)
        return JsonResponse("Failed to Add Property", safe=False)

    def put(self, request, id=None):
        book_to_update = Property.objects.get(id=id)
        serializer = PropertySerializer(
            instance=book_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Property updated Successfully", safe=False)
        return JsonResponse("Failed To Update Property")
