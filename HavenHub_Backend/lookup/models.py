from django.db import models
from property.models import Property


class Property_Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Property_Utility(models.Model):
    name = models.CharField(max_length=200)
    property = models.ManyToManyField(Property, blank=True)

    def __str__(self):
        return self.name


def uploaded_to(int, filename):
    return ("images/rooms/" + filename)

class Images(models.Model):
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(
        upload_to=uploaded_to, null=True, blank=True)

