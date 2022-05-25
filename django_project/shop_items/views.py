from django.shortcuts import render
from django.views.generic import ListView

from shop_items.models import ShopItem


class ShopItemsView(ListView):
    
    queryset = ShopItem.objects.all()
    template_name = 'shop_items/shop_items_list.html'
    context_object_name = 'shop_items'
    