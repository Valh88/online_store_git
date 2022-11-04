import json
import time
from requests import request
#celecy tasks
#docker run -p 6379:6379 redis


def payment_orders_service(card, order_id, price):
    time.sleep(5)
    url = 'http://0.0.0.0:9000/pay'
    data = {"card": card, "order_id": order_id, "price": price}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    result = request(method='POST', url=url, json=data, timeout=5, headers=headers)
    return result

