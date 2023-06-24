from django.urls import (
    path,
    include,
)
from .views import (
    PostViewSet,
  
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
