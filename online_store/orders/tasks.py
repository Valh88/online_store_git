from online_store.celery import app
from orders.models import Order
from .service import payment_orders_service


@app.task
def check_payment(card, order_id, price):
    """
        заносит в базу данные запроса об оплате
    """

    result = payment_orders_service(card, order_id, price).json()
    order_id = result['order_id']
    status = result['status']
    order = Order.objects.get(pk=order_id)
    if status == 'ok':
        order.status = 'p'
        order.errors = None
    else:
        errors = result['errors']
        order.status = 'e'
        order.errors = errors
    order.save()

