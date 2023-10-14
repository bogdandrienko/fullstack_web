from django.contrib import admin
from django.urls import path, include
from django_app import views

urlpatterns = [
    path("", views.index),
    #
    path("register_mvt/", views.register_mvt, name="register_mvt"),
    #
    # GET(list) | POST(create)
    path("api/resume/", views.resume),
    # GET(detail) | PUT(PATCH)) | DELETE(delete)
    # path("resume/<str:pk>", views.register_mvt),
]
