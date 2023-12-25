from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'currency_exchange.settings')

app = Celery('currency_exchange')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'monitor-currency-changes': {
        'task': 'currency_app.tasks.monitor_currency_changes',
        'schedule': crontab(minute='*/5'),
    },

}

app.autodiscover_tasks()