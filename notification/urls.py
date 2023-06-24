from django.urls import (
    path,
    include,
)
from rest_framework import routers
from .views import  NotificationViewSet

router = routers.DefaultRouter()
router.register(r'notification', NotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

