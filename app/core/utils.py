from django.conf import settings
import requests
from .models import Quote


def fetch_quotes() -> Quote:
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey={settings.ALPHAVANTAGE_API_KEY}"
    r = requests.get(url)
    data = r.json()
    quote = Quote.objects.create(price=data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    return quote
