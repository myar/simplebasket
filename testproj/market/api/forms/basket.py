from __future__ import unicode_literals

from django import forms

from market.models import Basket


class BasketForm(forms.ModelForm):

    class Meta:
        model = Basket
        fields = "__all__"
