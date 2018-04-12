
# -*- coding: utf-8 -*-

from django.db import models

PROD_APPLE = 1
PROD_ORANGE = 2
PROD_PLAIN = 3

TYPE_CHOICES = ((PROD_APPLE, u'Apple'),
                (PROD_ORANGE, u'Orange'),
                (PROD_PLAIN, u'plain'))


class Item(models.Model):

    type_product = models.IntegerField(choices=TYPE_CHOICES)
    weight = models.FloatField()
