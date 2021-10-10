from celery.task import task
from .utils import fetch_quotes


@task(name="checker_prices",)
def checker_prices():
    fetch_quotes()
