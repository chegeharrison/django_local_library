# Generated by Django 5.0.4 on 2024-05-06 09:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Language",
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
                (
                    "name",
                    models.CharField(
                        help_text="Enter the book's natural language(eg. English, French, Japanese etc.)",
                        max_length=200,
                        unique=True,
                    ),
                ),
            ],
        ),
    ]