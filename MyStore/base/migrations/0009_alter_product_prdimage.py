# Generated by Django 4.1.4 on 2023-01-01 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_rename_username_product_admins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PRDimage',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
