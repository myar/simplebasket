from __future__ import unicode_literals

from django.db import models

from .item import Item


class Basket(models.Model):

    name = models.CharField(max_length=250)
    capacity = models.FloatField()
    delete = models.BooleanField(default=False)


class ItemsBasket(models.Model):

    basket = models.ForeignKey(Basket, related_name='basket_items',
                               on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    weight = models.FloatField()
