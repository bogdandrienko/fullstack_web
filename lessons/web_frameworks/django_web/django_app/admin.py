from django.contrib import admin

from django_app import models

# Register your models here
admin.site.register(models.Category)
admin.site.register(models.Book)
admin.site.register(models.BookReview)
