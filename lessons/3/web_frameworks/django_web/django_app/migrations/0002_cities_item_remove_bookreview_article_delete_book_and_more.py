# Generated by Django 4.2.4 on 2023-09-03 06:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("django_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cities",
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
                ("name", models.CharField(max_length=300, verbose_name="Наименование")),
                (
                    "index",
                    models.CharField(
                        max_length=300, unique=True, verbose_name="Индекс города"
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("0", "Пункт отправки"),
                            ("1", "Пункт сортировки"),
                            ("2", "Пункт приёма"),
                        ],
                        default="0",
                        max_length=300,
                        verbose_name="Тип отделения(сортировка/приём)",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Активность"),
                ),
            ],
            options={
                "verbose_name": "Отделение",
                "verbose_name_plural": "Отделения",
                "ordering": ("-is_active", "type", "name"),
            },
        ),
        migrations.CreateModel(
            name="Item",
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
                    "track",
                    models.CharField(
                        max_length=500, unique=True, verbose_name="Трек код"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("0", "На проверке"),
                            ("1", "В пути"),
                            ("2", "Сортировка"),
                            ("3", "Ожидает получения"),
                            ("4", "Доставлено"),
                        ],
                        default="0",
                        max_length=300,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "target",
                    models.CharField(max_length=300, verbose_name="Пункт назначения"),
                ),
                (
                    "weight",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Вес"
                    ),
                ),
                (
                    "width",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Ширина"
                    ),
                ),
                (
                    "height",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Высота"
                    ),
                ),
                (
                    "depth",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Глубина"
                    ),
                ),
                (
                    "contact",
                    models.CharField(max_length=300, verbose_name="Наименование"),
                ),
                ("address", models.TextField(max_length=3000, verbose_name="Адрес")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Цена"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Активность"),
                ),
                (
                    "date_time_start",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Дата отправки"
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
                "ordering": ("-status", "-date_time_start"),
            },
        ),
        migrations.RemoveField(
            model_name="bookreview",
            name="article",
        ),
        migrations.DeleteModel(
            name="Book",
        ),
        migrations.DeleteModel(
            name="BookReview",
        ),
        migrations.DeleteModel(
            name="Category",
        ),
    ]
