from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from cart.cart import Cart
from .models import Order, OrderItem
from users.forms import RegisterForm


class OrderView(generic.CreateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'order/order.html', context={'form': RegisterForm})

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        if request.user.is_authenticated:
            delivery = request.POST.get('delivery')
            city = request.POST.get('city')
            address = request.POST.get('address')
            pay = request.POST.get('pay')
            order = Order.objects.create(user=request.user,
                                         city=city,
                                         address=address,
                                         delivery=delivery[0],
                                         type_pay=pay[0],
                                         status='w',
                                         price=cart.get_total_price())

            [OrderItem.objects.create(order=order,
                                      item=item['product'],
                                      price=item['price'],
                                      quantity=item['quantity']) for item in cart]
            cart.clear()
        return render(request, 'order/order.html', context={})


def order_view(request):
    return render(request, 'order/order.html', context={})
