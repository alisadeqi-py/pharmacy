# Generated by Django 3.2 on 2022-11-09 17:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phonenumber',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('09(1[0-9]|3[0-9]|2[0-9])-?[0-9]{3}-?[0-9]{4}')]),
        ),
    ]
