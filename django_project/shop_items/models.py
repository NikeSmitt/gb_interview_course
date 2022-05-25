import datetime

from django.db import models


class ShopItem(models.Model):
    """Товар в магазине"""
    
    title = models.CharField(max_length=100, db_index=True, verbose_name='Название товара')
    receipt_date = models.DateField(default=datetime.date.today, verbose_name='Дата поступления')
    price = models.DecimalField(decimal_places=2, max_digits=9, default=0, verbose_name='Цена товара')
    vendor_name = models.CharField(max_length=50, null=True, db_index=True, verbose_name='Имя поставщика')
    item_unit = models.CharField(max_length=10, verbose_name='Единица измерения', default='шт')
    
    def __str__(self):
        return self.title
    