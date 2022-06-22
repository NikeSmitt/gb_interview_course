from django import template
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site

from shop_items.models import Section

register = template.Library()


@register.simple_tag
def get_sections():
    # sections = Section.objects.all()
    sections = Section.on_site.all()
    site = Site.objects.get_current()
    return {'sections': sections, 'site': site}
