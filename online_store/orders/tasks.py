from online_store.celery import app

from .service import payment_orders_service


@app.task
def check_payment():
    payment_orders_service()
