from __future__ import unicode_literals

from django.test import TestCase

from market.api.forms import BasketForm


class FormTest(TestCase):
    '''
        Test for Basket's form
    '''
    def setUp(self):
        self.data = {'name': 'Test name for basket',
                     'capacity': 5}

    def test_form_of_registration(self):
        form = BasketForm(self.data)
        # check if with correct data form is valid
        self.assertTrue(form.is_valid())

        form = BasketForm({'name': 'Only name'})
        self.assertFalse(form.is_valid())

        form = BasketForm({'capacity': 'Only name'})
        self.assertFalse(form.is_valid())
