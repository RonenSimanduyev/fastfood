# Generated by Django 4.0.6 on 2022-07-28 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='IsGlutenFree',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='dish',
            name='IsVegeterian',
            field=models.BooleanField(default=False),
        ),
    ]