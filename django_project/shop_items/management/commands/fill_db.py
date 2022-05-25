import json

from django.core.management import BaseCommand

from shop_items.models import ShopItem


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        with open('db_data.json', encoding='utf-8') as f:
            data = json.JSONDecoder().decode(f.read())
            for item in data:
                ShopItem.objects.create(**item)
                
        print(f'{len(data)} items added to database')
            