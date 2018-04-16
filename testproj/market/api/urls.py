from django.urls import path

from .views import BasketList, BasketAdd

urlpatterns = [
    path('v1/list/', BasketList.as_view(), name='basket_list'),
    path('v1/basket/add/', BasketAdd.as_view(), name='basket_add'),
]
