# Generated by Django 4.0.1 on 2022-04-21 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0011_categories_slug_user_birth_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ads',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]