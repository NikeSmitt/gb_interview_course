import datetime

from django.contrib.sites.managers import CurrentSiteManager
from django.db import models
from . import Section
from django.contrib.sites.models import Site


class ShopItem(models.Model):
    """Товар в магазине"""
    
    title = models.CharField(max_length=100, db_index=True, verbose_name='Название товара')
    receipt_date = models.DateField(default=datetime.date.today, verbose_name='Дата поступления')
    price = models.DecimalField(decimal_places=2, max_digits=9, default=0, verbose_name='Цена товара')
    vendor_name = models.CharField(max_length=50, null=True, db_index=True, verbose_name='Имя поставщика')
    item_unit = models.CharField(max_length=10, verbose_name='Единица измерения', default='шт')
    image = models.ImageField(verbose_name='Изображение товара', upload_to='item_images', null=True)
    
    sections = models.ManyToManyField(Section, related_name='shop_items', verbose_name='Разделы')
    
    sites = models.ManyToManyField(Site, verbose_name='Принадлежность к сайтам')

    objects = models.Manager()
    on_site = CurrentSiteManager('sites')
    
    def __str__(self):
        return self.title
