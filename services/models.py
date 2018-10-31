from django.db import models
import uuid


class Product(models.Model):
    name = models.CharField(max_length=30)
    product_type = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

