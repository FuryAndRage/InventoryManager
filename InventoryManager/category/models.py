from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.CharField('Category', max_length = 100)

    def __str__(self):
        return self.category_name 
