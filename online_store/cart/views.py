from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from products.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django.views import generic
from django.urls import resolve


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data

        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
        if cd['update']:
            return redirect('cart')
    return redirect(request.META.get('HTTP_REFERER'))
    # return JsonResponse(data={}, status=200)


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart')


def cart_detail(request):
    form = CartAddProductForm()
    return render(request, 'cart/cart.html', context={'form_edit_quantity': form})


class CartDetail(generic.View):
    template_name = 'cart/cart.html'
