from django.contrib.auth.models import User, AbstractUser
from django.db import models


# Create your models here.

class Users(AbstractUser):
    balance = models.DecimalField(max_digits=9, decimal_places=2, default=0)


class Catalog(models.Model):
    enemy_f = models.CharField(max_length=255)
    enemy_s = models.CharField(max_length=255)
    rate = models.FloatField()
    end = models.DateField(auto_now=True)
    result = models.BooleanField(default=False)
    winner = models.CharField(max_length=300, choices=(('1', enemy_s), ('0', enemy_f), (None, None)), default=None,
                              blank=True)

    def __str__(self):
        return f"{self.enemy_s}:{self.enemy_f}"


class Orders(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.DO_NOTHING)
    choice = models.BooleanField()
    user = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    order_sum = models.DecimalField(max_digits=9, decimal_places=2)
