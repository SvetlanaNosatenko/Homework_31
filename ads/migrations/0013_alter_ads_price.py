# Generated by Django 4.0.1 on 2022-04-21 19:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0012_alter_ads_name_alter_ads_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]