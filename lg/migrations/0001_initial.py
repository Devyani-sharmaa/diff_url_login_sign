# Generated by Django 4.2.4 on 2024-09-23 06:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="add_product",
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
                ("product_name", models.CharField(max_length=50)),
                ("product_description", models.CharField(max_length=50)),
                ("price", models.CharField(max_length=50)),
            ],
        ),
    ]
