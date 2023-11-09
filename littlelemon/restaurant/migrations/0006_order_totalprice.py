# Generated by Django 4.2.7 on 2023-11-06 15:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0005_orderitem_orderid"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="totalPrice",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]