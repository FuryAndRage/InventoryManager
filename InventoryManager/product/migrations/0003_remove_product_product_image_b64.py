# Generated by Django 3.1.1 on 2020-09-23 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200923_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_image_b64',
        ),
    ]
