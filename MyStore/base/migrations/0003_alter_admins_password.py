# Generated by Django 4.1.4 on 2022-12-26 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_names_admins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admins',
            name='password',
            field=models.CharField(max_length=17),
        ),
    ]