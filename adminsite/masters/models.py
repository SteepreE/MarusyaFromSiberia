from django.db import models


class Stage(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Master(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    third_name = models.CharField(max_length=255, default='')

    phone_number = models.CharField(max_length=12)

    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    stage = models.ForeignKey(Stage, on_delete=models.SET_NULL, null=True)

    def get_name(self):
        return f"{self.second_name} {self.first_name} {self.third_name}"

    def __str__(self):
        return f"{self.second_name} {self.first_name}"
