from django.contrib import admin
from .models import Property_Utility, Property_Type, Images
# Register your models here.

admin.site.register(Property_Type)
admin.site.register(Property_Utility)
admin.site.register(Images)