from django.shortcuts import render
from rest_framework import viewsets
from category.models import (
    Category,
)
from category.serializers import (
    CategorySerializer,
)

class CategoryView(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
