from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShopItemsView.as_view())
]
