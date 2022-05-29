from django import template

from shop_items.models import Section

register = template.Library()


@register.simple_tag
def get_sections():
    sections = Section.objects.all()
    return sections
