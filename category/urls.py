from django.urls import (
    path,
    include,
)
from category import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'category', views.CategoryView)

urlpatterns = [
    path('', include(router.urls)),
]
