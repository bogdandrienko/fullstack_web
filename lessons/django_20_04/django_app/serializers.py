from rest_framework import serializers
from django_app import models


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Worker
        fields = '__all__'  # ['id', 'user', 'title', 'is_pay']
