# Generated by Django 4.0.2 on 2022-07-30 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_remove_dish_remove'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='dishes',
            field=models.ManyToManyField(to='orders.Dish'),
        ),
    ]
