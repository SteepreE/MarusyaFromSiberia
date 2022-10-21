from django.db import models


class Master(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    third_name = models.CharField(max_length=255, default='')

    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.second_name} {self.first_name}"
