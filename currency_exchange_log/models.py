from django.db import models
from django.contrib.auth.models import User

class UserAccessLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    browser = models.CharField(max_length=50)

class CurrencyPair(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pair_name = models.CharField(max_length=255)
    price = models.FloatField()
    
    def __str__(self):
        return f"{self.user.username} - {self.pair_name}"
