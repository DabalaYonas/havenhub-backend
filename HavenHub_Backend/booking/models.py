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


class Booking(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    guests = models.IntegerField()
    status = models.CharField(
        max_length=200, choices=STATUS, default=PEND, null=True, blank=True)

    def __str__(self):
        return str(self.start_date)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.status == PEND or self.status == ACC:
            self.property.is_available = False
            self.property.save()
