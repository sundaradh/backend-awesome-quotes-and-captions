from rest_framework import serializers

from .models import Category


# create serializers for category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
