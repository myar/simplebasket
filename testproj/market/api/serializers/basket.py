
# -*- coding: utf-8 -*-


def serialize(basket):

    serialized_basket = serialize_id(basket)

    serialized_basket.update({
        'name': basket.name,
        'capacity': basket.capacity,
        'delete': basket.delete,
    })

    return serialized_basket


def serialize_id(basket):
    return {
        'id': basket.id
    }
