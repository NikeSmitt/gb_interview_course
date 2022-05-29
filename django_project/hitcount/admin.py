from django.contrib import admin

from hitcount.models import HitCount


@admin.register(HitCount)
class HitCountAdmin(admin.ModelAdmin):
    list_display = ['user', 'url', 'count']
    search_fields = ['url']
    list_filter = ['user']