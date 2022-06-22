from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


app_name = 'shop_items'
urlpatterns = [
    path('', views.ShopItemsView.as_view(), name='items'),
    path('<slug:slug>', views.SectionItemsView.as_view(), name='section_items'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
