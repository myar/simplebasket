from __future__ import unicode_literals

import factory
import factory.fuzzy

from market.models import TYPE_CHOICES


class ItemFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'market.Item'

    type_product = factory.fuzzy.FuzzyChoice((1,2,3))
    weight = factory.fuzzy.FuzzyInteger(1000)


def instantiate_formset(formset_class, data, instance=None, initial=None):
    prefix = formset_class().prefix
    formset_data = {}
    for i, form_data in enumerate(data):
        for name, value in form_data.items():
            if isinstance(value, list):
                for j, inner in enumerate(value):
                    formset_data['{}-{}-{}_{}'.format(prefix, i, name, j)] = inner
            else:
                formset_data['{}-{}-{}'.format(prefix, i, name)] = value
    formset_data['{}-TOTAL_FORMS'.format(prefix)] = len(data)
    formset_data['{}-INITIAL_FORMS'.format(prefix)] = 0

    if instance:
        return formset_class(formset_data, instance=instance, initial=initial)
    else:
        return formset_class(formset_data, initial=initial)
