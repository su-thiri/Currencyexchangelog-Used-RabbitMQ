from django.db import models

class CurrencyPair(models.Model):
    pair_name = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
