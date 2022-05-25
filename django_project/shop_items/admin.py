from django.contrib import admin

from shop_items.models import ShopItem


@admin.register(ShopItem)
class ShopItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'vendor_name']
    list_display_links = ['id', 'title']