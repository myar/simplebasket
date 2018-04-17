from __future__ import unicode_literals

from django.db import models

from .item import Item


class LiveManager(models.Manager):

    def get_queryset(self):
        return super(LiveManager, self).get_queryset().filter(delete=False)


class Basket(models.Model):

    name = models.CharField(max_length=250)
    capacity = models.FloatField()
    delete = models.BooleanField(default=False)

    objects = LiveManager()

    def get_weight(self):
        total = 0
        for i in self.basket_items.all():
            total += i.weight
        return total


class ItemsBasket(models.Model):

    basket = models.ForeignKey(Basket, related_name='basket_items',
                               on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    weight = models.FloatField()
