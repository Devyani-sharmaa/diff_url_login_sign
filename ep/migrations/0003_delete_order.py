# Generated by Django 4.2.9 on 2024-09-25 09:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ep", "0002_order_delete_add_product"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Order",
        ),
    ]
