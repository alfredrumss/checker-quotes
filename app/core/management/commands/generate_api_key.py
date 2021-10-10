import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand
from rest_framework_api_key.models import APIKey


class Command(BaseCommand):
    """Django command to pause execution until db is available"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database connection')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
                self.stdout.write('generating api key...')
                api_key, key = APIKey.objects.create_key(name="checker_quote", prefix="chq_v1")
            except OperationalError:
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS(f"connection available and API KEY GENERATED! -> {key}"))
