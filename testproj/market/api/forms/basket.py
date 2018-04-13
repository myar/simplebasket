from __future__ import unicode_literals

from django import forms

from market.models import Basket


class BasketForm(forms.ModelForm):
    model = Basket
