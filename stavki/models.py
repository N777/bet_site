from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Users(User):
    balance = models.DecimalField(max_digits=9, decimal_places=2)


class Catalog(models.Model):
    enemy_f = models.CharField(max_length=255)
    enemy_s = models.CharField(max_length=255)
    rate = models.FloatField()
    end = models.DateField(auto_now=True)
    result = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.enemy_s}:{self.enemy_f}"


class Orders(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.DO_NOTHING)
    choice = models.BooleanField()
    user = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    order_sum = models.DecimalField(max_digits=9, decimal_places=2)
