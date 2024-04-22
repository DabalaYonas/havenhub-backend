from django.db import models
from property.models import Property
from user.models import User

ACC = "ACCEPTED"
CANC = "CANCELLED"
PEND = "PENDING"
RET = "RETURNED"

STATUS = ((ACC, "ACCEPTED"),
          (PEND, "PENDING"),
          (CANC, "CANCELLED"),
          (RET, "RETURNED"),
          )


class Sale(models.Model):
    closing_date = models.DateField()

    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.closing_date)