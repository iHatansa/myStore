# Generated by Django 4.1.4 on 2023-01-06 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0030_alter_admins_totalprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admins',
            name='totalprice',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
