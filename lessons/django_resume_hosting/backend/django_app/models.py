from django.core import validators
from django.db import models


class Resume(models.Model):
    first_name = models.CharField(verbose_name="Имя", max_length=300, validators=[validators.MinLengthValidator(3)])
    date = models.DateField(verbose_name="Дата рождения", blank=True, null=True, default=None)

    class Meta:
        app_label = "django_app"
        ordering = ("-first_name",)
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"
        db_table = "resume_model_table"  # RAW SQL

    def __str__(self):
        return f"<Resume {self.first_name}>"
