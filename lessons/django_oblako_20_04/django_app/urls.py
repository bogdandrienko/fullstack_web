from django.contrib import admin
from django.urls import path, include
from django_app import views

urlpatterns = [
    path("api/native", views.api_native),
    path("api/drf/<str:pk>/<str:category>", views.api_drf),
    # workers
    # REST-API/REST x3
    # GET(many), POST
    path("api/worker/", views.worker),
    # GET(one), DELETE, PUT
    path("api/worker/<str:pk>/", views.worker),
]
