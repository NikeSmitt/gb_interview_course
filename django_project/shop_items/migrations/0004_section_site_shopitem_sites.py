# Generated by Django 4.0.4 on 2022-06-05 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('shop_items', '0003_alter_section_description_alter_section_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site'),
        ),
        migrations.AddField(
            model_name='shopitem',
            name='sites',
            field=models.ManyToManyField(to='sites.site', verbose_name='Принадлежность к сайтам'),
        ),
    ]
