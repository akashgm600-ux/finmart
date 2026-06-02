from django.db import models

class Product(models.Model):
    TYPES = [('FD','Fixed Deposit'),('LOAN','Loan'),('INS','Insurance')]
    name       = models.CharField(max_length=200)
    type       = models.CharField(max_length=10, choices=TYPES)
    interest   = models.DecimalField(max_digits=5, decimal_places=2)
    min_amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.type})"