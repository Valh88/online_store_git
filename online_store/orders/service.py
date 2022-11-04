import json
import time
from requests import request
#celecy tasks
#docker run -p 6379:6379 redis


def payment_orders_service(card, order_id, price):
    """
    заглушка оплаты
    :param card: корзина
    :param order_id: заказ
    :param price: цена
    :return:
    """
    time.sleep(5)
    # url = 'http://localhost:9000/pay'
    # data = {"card": card, "order_id": order_id, "price": price}
    # headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    # result = request(method='POST', url=url, json=data, timeout=3, headers=headers)
    # card = data['card']
    # order_id = data['order_id']
    # price = data['price']
    if card[-1::] == '0':
        return {"status": "bad", "errors": "карта заканчивается на 0",
                        "order_id": order_id, "price": price}
    return {"status": "ok", "order_id": order_id, "price": price}


