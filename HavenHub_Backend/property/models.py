from django.db import models
from user.models import User
# from lookup.models import Property_Type, Property_Utility

def uploaded_to(int, filename):
    return ("images/property_ownerships/" + int.first_name + "_" + int.last_name + filename)


class Property(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True,
                              on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    # type = models.ForeignKey(Property_Type, on_delete=models.SET_NULL, null=True, blank=True)
    # utility = models.ManyToManyField(Property_Utility, blank=True)
    price_per_day = models.IntegerField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    auto_confirm  = models.BooleanField(default=True)
    with_furniture = models.BooleanField(default=True)

    #Selling properties
    property_ownership = models.CharField(max_length=200, null=True, blank=True)
    area_size = models.IntegerField(null=True, blank=True)
    sale_price = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # if self.model
        super().save(*args, **kwargs)

    def __str__(self):
        return self.address
