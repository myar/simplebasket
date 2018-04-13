from django.urls import path

from .views import BasketList

urlpatterns = [
    path('v1/list/', BasketList.as_view(), name='basket_list')

]
