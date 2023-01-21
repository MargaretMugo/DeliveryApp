from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=30)
    delivery_name = models.CharField(max_length=30)
    quantity = models.IntegerField()

    def __str__(self):
        return self.first_name

    def __str__(self):
        return self.last_name

    def body_preview(self):
        return self.delivery_name[:50]
