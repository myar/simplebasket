# simplebasket

API:

/api/v1/list/:

    GET-
        [{"id": somedata,
           "name": somedata,
           "capacity": somedata,
           "delete": somedata,
           "items_basket": [{
                             "id": somedata,
                             "weight": somedata,
                             "item": {"id": somedata,
                                      "weight": somedata,
                                      "type_product": somedata}
                            }]
        }]

/api/v1/basket/add/:
...
