# Generated by Django 4.1.4 on 2023-01-01 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_product_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='username',
            new_name='Admins',
        ),
    ]
