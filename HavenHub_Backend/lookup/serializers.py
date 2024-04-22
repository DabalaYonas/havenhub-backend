from rest_framework import serializers
from . import models


class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Property_Type
        fields = '__all__'


class PropertyUtilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Property_Utility
        fields = '__all__'


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Images
        fields = '__all__'

