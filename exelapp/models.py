from django.db import models


# Create your models here.
# class Order(models.Model):
#     order_id = models.CharField(max_length=100, unique=True)
#     product_name = models.CharField(max_length=100)
#     product_price = models.DecimalField(max_digits=10, decimal_places=2)
#     shipped = models.BooleanField()


class Order(models.Model):
    order_id = models.CharField(max_length=100, unique=True)
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipped = models.BooleanField(default=False)

    def __str__(self):
        return self.order_id
