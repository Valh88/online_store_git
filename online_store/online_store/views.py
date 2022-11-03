from django.shortcuts import render
from django.views import generic
from products.models import Catalog
from products.models import Product
from cart.forms import CartAddProductForm
from django import forms
from django.core.cache import cache


def index_page(request):
    products = Product.objects.all().select_related('catalog')
    catalog = cache.get_or_set('cat_key', Catalog.objects.only('name').filter(select_group=True), 60)
    # products_limited = cache.get_or_set('lim_key', products.filter(limited_edition=True), 60)
    # popular_product = cache.get_or_set('popular_key', products.all()[:8], 60)
    # catalog = Catalog.objects.only('name').filter(select_group=True)
    products_limited = products.filter(limited_edition=True)
    popular_product = products.all()[:8]
    form = CartAddProductForm()
    form.fields['quantity'].widget = forms.HiddenInput()
    return render(request, 'index.html', context={'catalog': catalog,
                                                  'limited': products_limited,
                                                  'popular': popular_product,
                                                  'form': form})
