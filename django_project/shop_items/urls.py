from django.urls import path
from . import views


app_name = 'shop_items'
urlpatterns = [
    path('', views.ShopItemsView.as_view(), name='items'),
    path('<slug:slug>', views.SectionItemsView.as_view(), name='section_items'),
]
