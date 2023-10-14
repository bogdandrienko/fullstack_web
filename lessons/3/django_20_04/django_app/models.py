from django.db import models


class Worker(models.Model):
    iin = models.CharField(verbose_name="ИИН", unique=True, max_length=13)
    first_name = models.CharField(verbose_name="Имя", max_length=200)
    last_name = models.CharField(verbose_name="Фамилия", max_length=200)

    class Meta:
        app_label = "django_app"
        ordering = ("iin",)
        verbose_name = "Работник"
        verbose_name_plural = "Работники"

    def __str__(self):
        return f"<Worker {self.iin} {self.first_name} {self.last_name}>"
