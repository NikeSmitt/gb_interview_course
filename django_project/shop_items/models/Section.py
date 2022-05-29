from django.db import models


class Section(models.Model):
    """Раздел товаров"""
    
    title = models.CharField(max_length=50, db_index=True, unique=True, verbose_name='Название раздела')
    description = models.CharField(max_length=500, blank=True, verbose_name='Описание раздела')
    slug = models.SlugField()
    
    def __str__(self):
        return self.title
