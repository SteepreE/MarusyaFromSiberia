from django.db import models

from masters.models import Master
from materials.models import Material


class Client(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    third_name = models.CharField(max_length=255, default='')

    phone_number = models.CharField(max_length=12)

    sale_size = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.second_name} {self.first_name} {self.third_name}"


class Stage(models.Model):
    name = models.CharField(max_length=255)

    master = models.ForeignKey(Master, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.master.__str__()}"


class Order(models.Model):
    product = models.CharField(max_length=255)
    sizes = models.TextField()
    details = models.TextField()

    materials = models.ManyToManyField(Material)

    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)

    current_stage = models.ForeignKey(Stage, on_delete=models.SET_NULL, null=True)

    price = models.FloatField()
    is_paid = models.BooleanField(default=False)

    order_date = models.DateField()

    def __str__(self):
        return self.product
