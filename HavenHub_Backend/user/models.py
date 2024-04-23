from django.db import models
from django.contrib.auth.models import AbstractUser

MAL = "Male"
FEM = "Female"

GENDER = ((MAL, "Male"),
          (FEM, "Female")
          )

def uploaded_to(int, filename):
    return ("images/profiles/" + int.first_name + "_" + int.last_name + filename)


def id_uploaded_to(int, filename):
    return ("images/IDs/" + int.first_name + "_" + int.last_name + filename)


# class User(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     email = models.EmailField()
#     password = models.CharField(max_length=200)
#     phone_number = models.CharField(max_length=200)
#     age = models.IntegerField()
#     gender = models.CharField(max_length=200, choices=GENDER)

#     profile_picture = models.ImageField(
#         upload_to=uploaded_to, width_field="width_length", height_field="heigth_length", null=True, blank=True)

#     id_picture = models.ImageField(
#         upload_to=id_uploaded_to, width_field="width_length", height_field="heigth_length", null=True, blank=True)
    
#     width_length = models.IntegerField(default=0, null=True, blank=True)
#     heigth_length = models.IntegerField(default=0, null=True, blank=True)


#     def __str__(self):
#         return (self.first_name + " " + self.last_name)

class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=200, choices=GENDER)
    username = None
    profile_picture = models.ImageField(
        upload_to=uploaded_to, width_field="width_length", height_field="heigth_length", null=True, blank=True)
    id_picture = models.ImageField(
        upload_to=id_uploaded_to, width_field="width_length", height_field="heigth_length", null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    width_length = models.IntegerField(default=0, null=True, blank=True)
    heigth_length = models.IntegerField(default=0, null=True, blank=True)