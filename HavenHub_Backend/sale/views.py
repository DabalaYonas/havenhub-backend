from .models import Sale
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from .serializers import SaleSerializer
from django.http import JsonResponse

class SaleView(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()

    def post(self, request):
        data = request.data
        serializer = SaleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Sale Added Successfully", safe=False)
        return JsonResponse("Failed to Add Sale", safe=False)

    def put(self, request, id=None):
        book_to_update = Sale.objects.get(id=id)
        serializer = SaleSerializer(
            instance=book_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Sale updated Successfully", safe=False)
        return JsonResponse("Failed To Update Sale")
