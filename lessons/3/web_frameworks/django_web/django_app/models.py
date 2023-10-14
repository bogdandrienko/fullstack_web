import random

from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator
from django.db import models
from django.utils.timezone import now


# Create your models here.
# Price - услуга (title: str, description: str, image: str(путь к картинке), price: float...)


# class Price:
#     """Эта цены на услуги"""
#
#     # <input type="text" required min=1 -- validator
#     # <input type="email" -- validator
#
#     # id = models.BigAutoField()  # SERIAL / AUTOINCREMENT
#     title = models.CharField(
#         # db_column='title_db_column',
#         db_index=True,
#         # db_tablespace="title_db_tablespace",
#         # error_messages=False,
#         # primary_key=False,
#         # validators=[  # - web framework validators
#         #     MinLengthValidator(0),
#         #     MaxLengthValidator(400),
#         # ],
#         # unique=False,
#         editable=True,
#         blank=True,
#         null=True,
#         default="",
#         verbose_name="Пароль",
#         help_text='<small class="text-muted">CharField [0, 300]</small><hr><br>',
#         max_length=250,
#     )  # VarChar(250)
#     # email = models.EmailField(validators=[EmailValidator])
#     # slug = models.SlugField(validators=[unicode])
#     # price = models.IntegerField(validators=[EmailValidator])
#     author = models.ForeignKey(  # OneToMany - только один из User
#         verbose_name="Связь к пользователям",
#         to=User,
#         on_delete=models.SET_NULL,  # CASCADE, DO_NOTHING , SET_DEFAULT , SET_NULL
#         related_name="author",
#     )
#     category = models.OneToOneField(  # OneToOne (ForeignKey(unique=True)) - только один из User к этой услуге
#         verbose_name="Связь к категории",
#         to=User,
#         on_delete=models.SET_NULL,  # CASCADE, DO_NOTHING , SET_DEFAULT , SET_NULL
#         related_name="author",
#     )
#     tags = models.ManyToManyField(  # ManyToMany - только один из User к этой услуге
#         verbose_name="Связь к тэгам",
#         to=User,
#         on_delete=models.SET_NULL,  # CASCADE, DO_NOTHING , SET_DEFAULT , SET_NULL
#         related_name="author",
#     )


# class Category(models.Model):
#     # id
#     name = models.CharField(verbose_name="Название", max_length=255)
#
#     def __str__(self):
#         return f"<Category {self.name}>"
#
#
# class Book(models.Model):
#     title = models.CharField(verbose_name="Наименование", max_length=255)
#     # ManyToMany - только один из User к этой услуге
#     categories = models.ManyToManyField(
#         verbose_name="Связь к категориям",
#         to=Category,
#         related_name="author",
#     )
#
#     def __str__(self):
#         return f"<Book {self.title}>"
#
#
# class BookReview(models.Model):
#     article = models.ForeignKey(
#         verbose_name="Связь к категории",
#         to=Book,
#         on_delete=models.SET_NULL,  # CASCADE, DO_NOTHING , SET_DEFAULT , SET_NULL
#         related_name="article",
#         null=True,
#     )
#     rating = models.IntegerField()
#
#     def __str__(self):
#         return f"<BookReview {self.rating}>"


class Cities(models.Model):
    """Список отделений"""

    LIST_DB_VIEW_CHOICES = [("0", "Пункт отправки"), ("1", "Пункт сортировки"), ("2", "Пункт приёма")]

    name = models.CharField(max_length=300, verbose_name="Наименование")
    index = models.CharField(max_length=300, verbose_name="Индекс города", unique=True)
    type = models.CharField(max_length=300, verbose_name="Тип отделения(сортировка/приём)", choices=LIST_DB_VIEW_CHOICES, default="0")
    is_active = models.BooleanField(default=True, verbose_name="Активность")

    class Meta:
        """Вспомогательный класс"""

        app_label = "django_app"
        ordering = ("-is_active", "type", "name")
        verbose_name = "Отделение"
        verbose_name_plural = "Отделения"

    def __str__(self):
        return self.name


def generate_track(length: int, characters: str) -> str:
    return "".join(random.choice(characters) for _ in range(length))


class Item(models.Model):
    #                        db       admin
    LIST_DB_VIEW_CHOICES = [("0", "На проверке"), ("1", "В пути"), ("2", "Сортировка"), ("3", "Ожидает получения"), ("4", "Доставлено")]

    track = models.CharField(verbose_name="Трек код", unique=True, max_length=500)
    # slug = models.CharField(verbose_name="Ссылка", unique=True, max_length=500)
    status = models.CharField(
        max_length=300, verbose_name="Статус", choices=LIST_DB_VIEW_CHOICES, default="0"
    )  # ибо таблица со статусами пока что примитивна
    target = models.CharField(max_length=300, verbose_name="Пункт назначения")

    weight = models.DecimalField(verbose_name="Вес", max_digits=10, decimal_places=2)
    width = models.DecimalField(verbose_name="Ширина", max_digits=10, decimal_places=2)
    height = models.DecimalField(verbose_name="Высота", max_digits=10, decimal_places=2)
    depth = models.DecimalField(verbose_name="Глубина", max_digits=10, decimal_places=2)

    contact = models.CharField(max_length=300, verbose_name="Наименование")
    address = models.TextField(max_length=3000, verbose_name="Адрес")

    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)

    is_active = models.BooleanField(verbose_name="Активность", default=True)
    date_time_start = models.DateTimeField(default=now, verbose_name="Дата отправки")

    class Meta:
        """Вспомогательный класс"""

        app_label = "django_app"
        ordering = ("-status", "-date_time_start")
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return f"<Item {self.address} {self.get_choice()}>"

    def get_choice(self):
        #                           k        v            0      1
        # LIST_DB_VIEW_CHOICES = [("0", "На проверке"), ("1", "В пути"),
        for c in self.LIST_DB_VIEW_CHOICES:
            if c[0] == self.status:
                return c[1]

    @staticmethod
    def price_formul(**kwargs) -> float:
        # Вычисляемое(динамическое) поле
        """Формула на основании место назначения и веса, объёма..."""

        return random.randint(1000, 100000)

    @staticmethod
    def track_generator() -> str:
        f1 = "NL"
        f2 = generate_track(4, "1234567890")
        f3 = generate_track(4, "1234567890")
        f4 = generate_track(3, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        # f1  f2   f3   f4
        # NL-1354-1342-KJG

        # UI - user interface (beaty)
        # UX - user experience (user friendly)
        # NL-5868-8592-OMC
        # NL-0085-6320-QTK
        # NL-1395-6601-RZP
        # 87712931237
        # 8 771 293 12 37
        return f"{f1}-{f2}-{f3}-{f4}"


class Tracking(models.Model):
    """Закреплённые товары для отслеживания"""

    # Получить все пользователей, кто прикреплён к этой посылке.
    # track
    # trackings = Tracking.objects.filter(items=item)
    # [QuerySet]
    # items.all()
    # items.filter()
    # items.add()
    # items.count()

    # ForeignKey(unique=True) === OneToOneField
    user = models.ForeignKey(verbose_name="Трек код", to=User, on_delete=models.CASCADE)
    tracks = models.ManyToManyField(verbose_name="Трек код", to=Item, blank=True)

    class Meta:
        """Вспомогательный класс"""

        app_label = "django_app"
        ordering = ("user",)
        verbose_name = "Отслеживание"
        verbose_name_plural = "Отслеживания"

    def __str__(self):
        return f"<Tracking {self.user.username} {self.tracks.count()}>"
