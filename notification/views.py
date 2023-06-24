from django.shortcuts import render
from rest_framework import viewsets

from .models import Notification
from .serializers import NotificationSerializer

# Create your views here.


class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer




