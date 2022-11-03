from django.urls import path
from .views import OrderView, order_view

urlpatterns = [
    path('order/', OrderView.as_view(), name='order')
]
