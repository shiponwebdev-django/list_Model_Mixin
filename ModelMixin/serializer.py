from rest_framework import serializers
from .models import ModelMixin


class ModelMixinSerializer(serializers.ModelSerializer):

    class Meta:
        model = ModelMixin
        fields =['name', 'roll', 'department', 'subject']
