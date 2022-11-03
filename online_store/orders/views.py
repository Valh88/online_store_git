from django.shortcuts import render
from django.views import generic
from .forms import OrderForm
from cart.cart import Cart
from .models import Order, OrderItem


class OrderView(generic.CreateView):
    # template_name = 'order/order.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'order/order.html', context={})

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        mail = request.POST.get('mail')
        delivery = request.POST.get('delivery')
        city = request.POST.get('city')
        address = request.POST.get('address')
        pay = request.POST.get('pay')

        cart = Cart(request)
        if request.user.is_authenticated:
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
        else:
            pass
        print(name, phone, mail, delivery, city, address, pay)
        return render(request, 'order/order.html', context={})


def order_view(request):
    return render(request, 'order/order.html', context={})
