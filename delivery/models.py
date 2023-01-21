from django.db import models


class Delivery(models.Model):
    delivery_name = models.CharField(max_length=30)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.delivery_name

    def body_preview(self):
        return self.description[:50]
