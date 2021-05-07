from django.db import models

# Create your models here.


class HistoricalData(models.Model):
    ticker = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=False)
    open = models.DecimalField(max_digits=19, decimal_places=2)
    high = models.DecimalField(max_digits=19, decimal_places=2)
    low = models.DecimalField(max_digits=19, decimal_places=2)
    close = models.DecimalField(max_digits=19, decimal_places=2)
    adj_close = models.DecimalField(max_digits=19, decimal_places=2)
    volume = models.IntegerField()
