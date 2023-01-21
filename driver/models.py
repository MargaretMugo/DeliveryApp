from django.db import models


class Driver(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=30)
    delivery_name = models.CharField(max_length=30)
    license_plate = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

    def __str__(self):
        return self.last_name

    def body_preview(self):
        return self.delivery_name[:50]
