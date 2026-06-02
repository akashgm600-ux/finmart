from django.db import models
from django.conf import settings

class Order(models.Model):
    STATUS  = [('PENDING','Pending'),('ACTIVE','Active'),('CLOSED','Closed')]
    user    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    account = models.ForeignKey('accounts.BankAccount', on_delete=models.CASCADE)
    amount  = models.DecimalField(max_digits=12, decimal_places=2)
    status  = models.CharField(max_length=10, choices=STATUS, default='PENDING')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} — {self.user.username}"

class Transaction(models.Model):
    order   = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount  = models.DecimalField(max_digits=12, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction #{self.id} — ₹{self.amount}"