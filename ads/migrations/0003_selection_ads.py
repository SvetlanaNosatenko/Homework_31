# Generated by Django 4.0.1 on 2022-03-28 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_selection'),
    ]

    operations = [
        migrations.AddField(
            model_name='selection',
            name='ads',
            field=models.ManyToManyField(to='ads.Ads'),
        ),
    ]