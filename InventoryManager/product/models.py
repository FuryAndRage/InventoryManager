from django.db import models
from InventoryManager.category.models import Category
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name = 'Category')
    product_name = models.CharField('Product', max_length = 255)
    product_description = models.TextField(null = True)
    product_quantity = models.IntegerField(default = 0)
    product_image = models.ImageField(upload_to = 'product/')

    def __str__(self):
        return self.product_name
