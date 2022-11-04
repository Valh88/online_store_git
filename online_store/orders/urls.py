from django.urls import path
from .views import OrderView, process_pay

urlpatterns = [
    path('order/', OrderView.as_view(), name='order'),
    path('pay/', process_pay, name='pay'),
]
