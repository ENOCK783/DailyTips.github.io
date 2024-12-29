from django.db import models
from django.contrib.auth.models import User

class Tip(models.Model):
    match = models.CharField(max_length=255)
    tip = models.CharField(max_length=255)
    odds = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.match} - {self.tip}"

