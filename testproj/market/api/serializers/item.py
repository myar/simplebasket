
# -*- coding: utf-8 -*-


def serialize(item):

    serialized_item = {
        'id': item.id,
        'type_product': item.type_product,
        'weight': item.weight,
    }

    return serialized_item
