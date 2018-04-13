from __future__ import unicode_literals

from .item import serialize as serialize_item


def serialize(basket):

    serialized_basket = serialize_id(basket)

    serialized_basket.update({
        'name': basket.name,
        'capacity': basket.capacity,
        'delete': basket.delete,
        'items_basket': list(map(serialize_basket_items,
                             basket.basket_items.select_related()))
    })

    return serialized_basket


def serialize_basket_items(item):

    serialized_items = serialize_id(item)

    serialized_items.update({
        'item': serialize_item(item.item),
        'weight': item.weight,
    })
    return serialized_items


def serialize_id(data):
    return {
        'id': data.id
    }
