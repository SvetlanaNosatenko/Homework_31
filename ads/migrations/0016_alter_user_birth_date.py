# Generated by Django 4.0.1 on 2022-04-24 13:42

import ads.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0015_alter_ads_description_alter_ads_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(null=True, validators=[ads.models.check_birth_date]),
        ),
    ]
