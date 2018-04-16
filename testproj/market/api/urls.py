from django.urls import path

from .views import BasketList, BasketAdd, BasketDetail

urlpatterns = [
    path('v1/list/', BasketList.as_view(), name='basket_list'),
    path('v1/basket/add/', BasketAdd.as_view(), name='basket_add'),
    path('v1/basket/<int:pk>/', BasketDetail.as_view(),
         name='basket_detail'),
]
