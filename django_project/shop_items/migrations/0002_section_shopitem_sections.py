# Generated by Django 4.0.4 on 2022-05-28 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Раздел товаров')),
                ('description', models.CharField(max_length=500, verbose_name='Описание раздела')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='shopitem',
            name='sections',
            field=models.ManyToManyField(related_name='shot_items', to='shop_items.section'),
        ),
    ]
