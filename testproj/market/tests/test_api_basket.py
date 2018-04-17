from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from market.models import Basket, Item

from .helpers import ItemFactory


class RegistrationTest(TestCase):
    '''
        Test for add basket
    '''
    def setUp(self):
        self.data = {'name': 'Test name for basket',
                     'capacity': 2222}
        self.url = reverse('basket_add')
        self.client.post(self.url, self.data, follow=True)

    def test_create_basket(self):

        basket_all = Basket.objects.all()
        self.assertEqual(basket_all.count(), 1)

        response = self.client.post(self.url, self.data, follow=True)
        self.assertEqual(response.status_code, 200)

        basket_all = Basket.objects.all()
        self.assertEqual(basket_all.count(), 2)

    def test_get_detail(self):

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

    def test_delete_basket(self):
        basket = list(Basket.objects.all())[-1]
        url = reverse('basket_detail', kwargs={'pk': basket.id})
        name = u'New 888888888888'
        self.data.update({'pk': basket.id, 'name': name})
        self.client.post(url, self.data, follow=True)

        response = self.client.delete(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, name)

        url = reverse('basket_detail', kwargs={'pk': 999})
        response = self.client.delete(url, follow=True)
        self.assertEqual(response.status_code, 404)

    def test_basket_items(self):
        basket = list(Basket.objects.all())[-1]
        item = ItemFactory()
        item2 = ItemFactory()
        url = reverse('basket_items', kwargs={'pk': basket.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        data = {
             'TOTAL_FORMS': 2,
             'item-0-item': item.id,
             'item-0-weight': 999,
             'item-1-item': item2.id,
             'item-1-weight': 888,
        }
        response = self.client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, item.weight)


        data2 = {
             'TOTAL_FORMS': 1,
             'item-0-item': item.id,
             'item-0-delete': 1,
        }
        response = self.client.post(url, data2, follow=True)
        self.assertNotContains(response, item.weight)

        response = self.client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 422)
        self.assertContains(response, 'Weight is too big', status_code=422)
