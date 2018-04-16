from __future__ import unicode_literals

import json

from django.views.generic import View, DetailView
from django.shortcuts import redirect, get_object_or_404
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


class BasketDetail(DetailView):

    model = Basket

    def get(self, request, *args, **kwargs):

        self.object = self.get_object()
        return self.render_to_response(basket.serialize(self.object))

    def post(self, request, *args, **kwargs):

        item = get_object_or_404(Basket, id=kwargs.get('pk', None))
        form = BasketForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return self.render_to_response(basket.serialize(item))
        raise ValidationError

    def render_to_response(self, result, response_class=HttpResponse):
        return response_class(json.dumps(result),
                              content_type='application/json')
