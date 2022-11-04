from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from cart.cart import Cart
from django.views.decorators.http import require_POST
from .models import Order, OrderItem
from users.forms import RegisterForm
from .tasks import check_payment
from .forms import PaymentForm


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
            form = PaymentForm(initial={'order': order.pk})
            if pay == 'online':
                return render(request, 'order/payment.html', context={'form': form})
            else:
                return render(request, 'order/paymentsomeone.html', context={'form': form})
        return render(request, 'order/order.html', context={})


@require_POST
def process_pay(request):
    form = PaymentForm(request.POST)
    if form.is_valid():
        order = form.cleaned_data['order']
        card = form.cleaned_data['num_card']
        order = Order.objects.get(pk=order)
        order_id = order.pk
        price = order.price

        check_payment.delay(card, order_id, price)
        return HttpResponseRedirect(reverse('account'))
