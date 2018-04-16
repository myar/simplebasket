from __future__ import unicode_literals

import json

from django.views.generic import View
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from market.models import Basket
from market.api.forms import BasketForm
from market.api.serializers import basket


class BasketList(View):

    def get(self, request, *args, **kwargs):

        baskets = Basket.objects.select_related()

        return self.render_to_response(list(map(basket.serialize, baskets)))

    def render_to_response(self, result, response_class=HttpResponse):
        return response_class(json.dumps(result),
                              content_type='application/json')


class BasketAdd(View):

    def post(self, request, *args, **kwargs):

        form = BasketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('basket_list')
        raise ValidationError

    def render_to_response(self, result, response_class=HttpResponse):
        return response_class(json.dumps(result),
                              content_type='application/json')
