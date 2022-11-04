import json

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/pay', methods=['POST'])
def create_pay():
    """
    сервис оплаты товара
    """
    if request.is_json:
        data = request.get_json(force=True)
        card = data['card']
        order_id = data['order_id']
        price = data['price']
        if card[-1::] == '0':
            print(123123123123)
            return jsonify({"status": "bad", "errors": "карта заканчивается на 0",
                            "order_id": order_id, "price": price})
        return jsonify({"status": "ok", "order_id": order_id, "price": price})
    else:
        'error404'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)

