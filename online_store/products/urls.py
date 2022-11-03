from django.urls import path
from .views import ProductListView, ProductDetailView, tag_render, category_product
from .models import Product

from rest_framework import routers
from .api import ProductViewSet, CatalogViewSet

router = routers.DefaultRouter()
router.register('api/products', ProductViewSet)
router.register('api/catalog', CatalogViewSet)

urlpatterns = [
    path('catalog/', ProductListView.as_view(), name='catalog'),
    # path('catalog/<slug:cat_name>/', ProductListView.as_view(), name='menu'),
    path('catalog/<slug:cat_name>/', category_product, name='menu'),

    path('catalog/sort/price/', ProductListView.as_view(queryset=Product.objects.select_related('catalog').order_by('price')),
         name='sort_price'),
    path('catalog/sort/updated/', ProductListView.as_view(queryset=Product.objects.select_related('catalog').order_by('-updated')),
         name='sort_update'),
    path('catalog/product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('catalog/tag/<slug:tag_slug>/', tag_render, name='news_list_by_tag'),
] + router.urls
