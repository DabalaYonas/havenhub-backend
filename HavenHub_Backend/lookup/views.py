from rest_framework import viewsets
from . import serializers, models
from django.http import JsonResponse

class TypeView(viewsets.ModelViewSet):
    serializer_class = serializers.PropertyTypeSerializer
    queryset = models.Property_Type.objects.all()

    def post(self, request):
        data = request.data
        serializer = serializers.PropertyTypeSerializer(data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Property Types Saved Successfully", safe=False)
        return JsonResponse("Failed To Save Property Types")

    def put(self, request, id=None):
        model_to_update = models.Property_Type.objects.get(id=id)
        serializer = serializers.PropertyTypeSerializer(
            instance=model_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Property Types updated Successfully", safe=False)
        return JsonResponse("Failed To Update Property Types")

class UtilityView(viewsets.ModelViewSet):
    serializer_class = serializers.PropertyUtilitySerializer
    queryset = models.Property_Utility.objects.all()

    def post(self, request):
        data = request.data
        serializer = serializers.PropertyUtilitySerializer(data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Property Utility Saved Successfully", safe=False)
        return JsonResponse("Failed To Save Property Utility")

    def put(self, request, id=None):
        data_to_update = models.Property_Utility.objects.get(id=id)
        serializer = serializers.PropertyUtilitySerializer(
            instance=data_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Property Utility updated Successfully", safe=False)
        return JsonResponse("Failed To Update Property Utility")


class ImageView(viewsets.ModelViewSet):
    serializer_class = serializers.ImagesSerializer
    queryset = models.Images.objects.all()

    def post(self, request):
        data = request.data
        serializer = serializers.ImagesSerializer(data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Images Saved Successfully", safe=False)
        return JsonResponse("Failed To Save Images")

    def put(self, request, id=None):
        data_to_update = models.Images.objects.get(id=id)
        serializer = serializers.ImagesSerializer(
            instance=data_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Images updated Successfully", safe=False)
        return JsonResponse("Failed To Update Images")
