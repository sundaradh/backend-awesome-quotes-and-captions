from django.urls import (
    path,
    include,
)
from users import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserView)

urlpatterns = [
    path('', include(router.urls)),
]
