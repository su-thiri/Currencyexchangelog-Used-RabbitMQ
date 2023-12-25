# currency_app/tasks.py

from celery import Celery
from django.core.mail import send_mail
from .models import CurrencyPair
import requests

app = Celery('currency_app', broker='pyamqp://guest:guest@localhost//')

@app.task
def monitor_currency_changes():
    # Logic to monitor currency changes and notify users
    currency_pairs = CurrencyPair.objects.all()

    for currency_pair in currency_pairs:
        # Fetch the latest currency data from the API
        api_url = f'https://open.er-api.com/v6/latest/{currency_pair.pair_name}'
        response = requests.get(api_url)

        if response.status_code == 200:
            currency_data = response.json()
            current_price = currency_data.get('rates', {}).get(currency_pair.pair_name)

            if current_price is not None:
                # Check for price change
                price_change_threshold = 0.5
                if abs(current_price - currency_pair.price) > price_change_threshold:
                    # Notify user about the price change
                    notify_user(currency_pair.user, currency_pair.pair_name, current_price, currency_pair.price)

                    # Update the stored price
                    currency_pair.price = current_price
                    currency_pair.save()

def notify_user(user, pair_name, current_price, previous_price):
    # Example: Send email notifications to users
    subject = f'Currency Change Alert: {pair_name}'
    message = f'The price of {pair_name} has changed from {previous_price} to {current_price}.'
    send_mail(subject, message, 'thirishwehlaing9@gmail.com', [user.email])
