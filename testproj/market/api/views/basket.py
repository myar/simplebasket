from __future__ import unicode_literals

import json

from django.views.generic import View, DetailView
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from market.models import Basket, ItemsBasket
from market.api.forms import BasketForm, ItemsBasketForm
from market.api.serializers import basket


class BasketList(View):

    def get(self, request, *args, **kwargs):

        baskets = Basket.objects.select_related()
        return self.render_to_response(list(map(basket.serialize, baskets)))

    def render_to_response(self, result, status=200):
        return HttpResponse(json.dumps(result), status=status)


class BasketAdd(View):

    def post(self, request, *args, **kwargs):

        form = BasketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('basket_list')
        raise ValidationError

    def render_to_response(self, result, status=200):
        return HttpResponse(json.dumps(result), status=status)


class BasketDetail(DetailView):

    model = Basket

    def get(self, request, *args, **kwargs):

        self.object = self.get_object()
        return self.render_to_response(basket.serialize(self.object))

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        form = BasketForm(request.POST, instance=self.object)
        if form.is_valid():
            form.save()
            return self.render_to_response(basket.serialize(self.object))
        return self.render_to_response({'message': 'Form is invalide'},
                                       status=422)

    def delete(self, request, *args, **kwargs):

        self.object = self.get_object()
        self.object.delete = True
        self.object.save()
        return redirect('basket_list')

    def render_to_response(self, result, status=200):
        return HttpResponse(json.dumps(result), status=status)


class BasketItems(BasketDetail):

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        data = request.POST
        count = data.get('TOTAL_FORMS', None)
        total_weight = self.object.get_weight()
        for i in range(int(count)):
            item_data = {'item': data.get('item-%d-item' % i, None),
                         'weight': float(data.get('item-%d-weight' % i, 0)),
                         'basket': self.object.id,
                         'delete': data.get('item-%d-delete' % i, None)}
            form = ItemsBasketForm(item_data)
            if form.is_valid():
                if item_data['delete']:

                    item = ItemsBasket.objects.get(basket=self.object,
                                                   item=item_data['item'])
                    total_weight -= item.weight
                    item.delete()
                else:
                    total_weight += item_data['weight']
                    if self.object.capacity > total_weight:
                        form.save()
                    else:
                        return self.render_to_response(
                            {'message': 'Weight is too big'},
                            status=422)
        return redirect('basket_items', pk=self.object.id)
