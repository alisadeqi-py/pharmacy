# Generated by Django 3.2 on 2022-11-09 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='special',
            field=models.BooleanField(default=False),
        ),
    ]
