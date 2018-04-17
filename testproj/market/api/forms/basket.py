from __future__ import unicode_literals

from django import forms

from market.models import Basket, ItemsBasket


class BasketForm(forms.ModelForm):

    class Meta:
        model = Basket
        fields = "__all__"


class ItemsBasketForm(forms.ModelForm):

    class Meta:
        model = ItemsBasket
        fields = "__all__"
