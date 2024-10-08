# Generated by Django 4.2.9 on 2024-09-25 05:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ep", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_category", models.CharField(max_length=20)),
                ("payment_method", models.CharField(max_length=50)),
                ("shipping_cost", models.CharField(max_length=50)),
                ("unit_price", models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.DeleteModel(
            name="add_product",
        ),
    ]
