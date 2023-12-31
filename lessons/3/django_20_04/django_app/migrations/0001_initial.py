# Generated by Django 4.2.5 on 2023-09-16 05:36

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Worker",
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
                    "iin",
                    models.CharField(max_length=13, unique=True, verbose_name="ИИН"),
                ),
                ("first_name", models.CharField(max_length=200, verbose_name="Имя")),
                ("last_name", models.CharField(max_length=200, verbose_name="Фамилия")),
            ],
            options={
                "verbose_name": "Работник",
                "verbose_name_plural": "Работники",
                "ordering": ("iin",),
            },
        ),
    ]
