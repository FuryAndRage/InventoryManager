from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'category','product_name', 'product_quantity')
    search_fields = ('product_name',)
