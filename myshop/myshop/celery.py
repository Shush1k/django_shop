import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

app = Celery('myshop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
# celery -A myshop worker -l info
# celery -A myshop flower

# в команде выше `myshop` - это название, которое лежит в app = Celery('myshop')
