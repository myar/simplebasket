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
                     'capacity': 5}
        self.url = reverse('basket_add')
        self.form = BasketForm

    def test_create_basket(self):
        basket_all = Basket.objects.all()
        self.assertEqual(basket_all.count(), 0)

        response = self.client.post(self.url, self.data, follow=True)
        self.assertEqual(response.status_code, 200)

        basket_all = Basket.objects.all()
        self.assertEqual(basket_all.count(), 1)

    def test_get_detail(self):
        self.client.post(self.url, self.data, follow=True)

        basket = list(Basket.objects.all())[-1]
        url = reverse('basket_detail', kwargs={'pk': basket.id})
        response = self.client.get(url)
        self.assertContains(response, self.data['name'])
        self.assertContains(response, self.data['capacity'])

        name = u'New Test Name For test'
        self.data.update({'pk': basket.id, 'name': name})
        response = self.client.post(url, self.data, follow=True)
        self.assertEqual(response.status_code, 200)

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.data['name'])
        basket = self.assertEqual(list(Basket.objects.all())[-1].name, name)
