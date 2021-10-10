from django.db import models


class Quote(models.Model):
    price = models.CharField(
        max_length=100,
        verbose_name="Price",
    )
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)
