from django.urls import path
from .views import ShopSearchView

urlpatterns = [
    path('search/', ShopSearchView.as_view(), name='shop-search'),
]
