# Generated by Django 4.0.4 on 2022-06-10 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_items', '0005_alter_section_managers_alter_shopitem_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopitem',
            name='image',
            field=models.ImageField(null=True, upload_to='media', verbose_name='Изображение товара'),
        ),
    ]
