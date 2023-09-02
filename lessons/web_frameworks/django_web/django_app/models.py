from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator
from django.db import models

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


class Category(models.Model):
    name = models.CharField(verbose_name="Название", max_length=255)

    def __str__(self):
        return f"<Category {self.name}>"


class Book(models.Model):
    title = models.CharField(verbose_name="Наименование", max_length=255)
    # ManyToMany - только один из User к этой услуге
    categories = models.ManyToManyField(
        verbose_name="Связь к категориям",
        to=Category,
        related_name="author",
    )

    def __str__(self):
        return f"<Book {self.title}>"


class BookReview(models.Model):
    article = models.ForeignKey(
        verbose_name="Связь к категории",
        to=Book,
        on_delete=models.SET_NULL,  # CASCADE, DO_NOTHING , SET_DEFAULT , SET_NULL
        related_name="article",
        null=True,
    )
    rating = models.IntegerField()

    def __str__(self):
        return f"<BookReview {self.rating}>"
