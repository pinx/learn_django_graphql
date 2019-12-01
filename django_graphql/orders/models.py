from django.db import models
from django.utils import timezone


class Order(models.Model):
    reference = models.CharField(max_length=50)
    ordered_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.reference


class OrderProduct(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE)
    product_id = models.UUIDField(null=True)
    quantity = models.FloatField(null=True)
