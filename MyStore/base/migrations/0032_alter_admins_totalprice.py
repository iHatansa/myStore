# Generated by Django 4.1.4 on 2023-01-06 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0031_alter_admins_totalprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admins',
            name='totalprice',
            field=models.IntegerField(max_length=10),
        ),
    ]
