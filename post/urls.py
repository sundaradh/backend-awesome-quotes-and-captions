from django.urls import (
    path,
    include,
)
from .views import (
    PostViewSet,
    PrivacyPolicy
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('privacy-policy/', PrivacyPolicy.as_view(), name='privacy-policy'),
]
