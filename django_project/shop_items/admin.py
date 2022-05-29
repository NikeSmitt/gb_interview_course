from django.contrib import admin

from shop_items.models import ShopItem, Section


@admin.register(ShopItem)
class ShopItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'vendor_name']
    list_display_links = ['id', 'title']


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']
