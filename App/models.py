from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    amount = models.FloatField()
    description = models.CharField(max_length=200)
    date = models.DateField()
    debit = models.BooleanField(default=False)
    balance = models.FloatField()

    def __str__(self):
        return self.description

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(default=0, max_digits=10, decimal_places=2)
