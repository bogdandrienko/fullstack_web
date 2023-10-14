from rest_framework import serializers
from django_app import models


class ResumeSerializer(serializers.ModelSerializer):
    # TODO ...

    class Meta:
        model = models.Resume
        fields = "__all__"  # ['id', 'first_name']
