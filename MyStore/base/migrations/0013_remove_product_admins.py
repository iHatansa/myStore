# Generated by Django 4.1.4 on 2023-01-01 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_product_admins'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Admins',
        ),
    ]
