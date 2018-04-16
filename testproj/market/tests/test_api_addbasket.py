from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from market.api.forms import BasketForm
from market.models import Basket


class RegistrationTest(TestCase):
    '''
        Test for add basket
    '''
    def setUp(self):
        self.data = {'name': 'Test name for basket',
                     'capacity ': 5}
        self.url = reverse('basket_add')
        self.form = BasketForm

    def test_create_basket(self):
        basket_all = Basket.objects.all()
        self.assertEqual(basket_all.count(), 0)

        response = self.client.post(self.url, self.data, follow=True)
        self.assertEqual(response.status_code, 200)

        basket_all = Basket.objects.all()
        self.assertEqual(basket_all.count(), 1)

