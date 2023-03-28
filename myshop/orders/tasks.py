from celery import shared_task
from django.core.mail import send_mail
from myshop.celery import app
from .models import Order
from django.conf import settings


@shared_task
def order_created(order_id, order_first_name, order_email):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    # order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order_id}'
    message = f'Dear {order_first_name},\n\n' \
              f'You have successfully placed an order.' \
              f'Your order ID is {order_id}.'
    mail_sent = send_mail(subject,
                          message,
                          settings.EMAIL_HOST_USER,
                          [order_email])
    return mail_sent


@app.task()
def test_task():
    print('Worked ')
    return True
