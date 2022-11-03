from .views import review_add_to_product
from django.urls import path


urlpatterns = [
    path('product/<int:product_id>/review/', review_add_to_product, name='review'),
]
