from django.db import models
from InventoryManager.product.models import Product
from django.contrib.auth.models import User


class WithdrawalProduct(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    withdrawal_time = models.DateTimeField(auto_now=True)
    withdrawal_quantity = models.IntegerField()
    withdrawal_reason = models.TextField(max_length=255)

    def __str__(self):
        return str(self.product)
