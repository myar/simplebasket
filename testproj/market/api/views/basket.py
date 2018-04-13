from __future__ import unicode_literals

import json

from django.views.generic import View
from django.http import HttpResponse

from market.models import Basket
from market.api.serializers import basket


class BasketList(View):

    def get(self, *args, **kwargs):

        baskets = Basket.objects.all()

        return self.render_to_response(list(map(basket.serialize, baskets)))

    def render_to_response(self, result, response_class=HttpResponse):
        return response_class(json.dumps(result),
                              content_type='application/json')
