from django.shortcuts import render
from django.views.generic import ListView, DetailView

from shop_items.models import ShopItem, Section


class ShopItemsView(ListView):
    
    queryset = ShopItem.objects.prefetch_related('sections').all()
    template_name = 'shop_items/shop_items_list.html'
    context_object_name = 'shop_items'
    
    
class SectionItemsView(ShopItemsView):
    
    def get_queryset(self):
        section_slug = self.kwargs.get('slug')
        return Section.objects.prefetch_related('shop_items').get(slug=section_slug).shop_items.all()
    