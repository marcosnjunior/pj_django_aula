# Generated by Django 5.0.6 on 2024-07-05 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("loja", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Fornecedor",
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
                ("nome", models.CharField(max_length=200)),
                ("endereco", models.CharField(max_length=500)),
            ],
        ),
    ]