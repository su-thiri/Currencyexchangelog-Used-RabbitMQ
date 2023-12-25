# Install django-5.0
# pip install django

# Install celery-5.3.6
# pip install celery

# There are two application folders as below :
# 1 . currency_app
# 2 . currency_exchange_log

# currency_app is for worker service to connect rabbitmq
# currency_exchange_log is for useraccess log (country , browser )

# Install rabbitmq-server
# sudo apt-get install rabbitmq-server ( on Linux Terminal )

# enable rabbitmq-service
# sudo systemctl enable rabbitmq-server

# start rabbitmq-service
# sudo systemctl start rabbitmq-server


# Check the status of rabbitmq-server
# systemctl status rabbitmq-server

# Example checked status of rabbitmq-server
# 24 02:02:07 tina systemd[1]: Starting RabbitMQ Messaging Server...
# 24 02:02:10 tina systemd[1]: Started RabbitMQ Messaging Server.

# add celery.py file in project folder
# add new application folder for monitoring currency exchange
# add new application name in setting.py of project folder
# add the model class for user_access_log in currency_exchange_log app
# add the model class for currency_pair in currency_app

# config celery in project to use as worker
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'currency_exchange.settings')

app = Celery('currency_exchange')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# start worker celery
# celery -A currency_exchange worker -l info

# install requests
# pip install requests

# config tasks.py to use celery as an worker service using rabbitmq

# run this command to ensure that Celery application is properly configured and Celery worker will connect to RabbitMQ which is running and configured correctly or not.

# celery -A currency exchange worker -l info

# use library to adjust the time for 5 mins


# Testing with seprate teminal and the output or result will show every 5 mins or USD chagned 0.5 than pervious currency rate


# run this command in sperate teminal
# python manage.py runserver
# celery -A currency_exchange beat -l info ( to know currency exchange )
# celery -A currency exchange worker -l info ( to know the message recieved log and successed log )

# to send the notification , please put your email as below -
# send_mail(subject, message, 'thirishwehlaing9@gmail.com', [user.email])

# Note :
# you can register with your real email account , if you want to test it you can use test email account
# With your test email, you will not see the notification of USD currency exchange (0.5) .
# With your real email, you can get notification of USD currency exchange (0.5).
# However if there is no currency changes , my system will not inform you .
# So please see the notification in every 5 minutes. 
