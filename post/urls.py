from django.urls import (
    path,
    include,
)
from .views import (
    PostViewSet,
    LikeCreateView,
    FavoriteCreateView,
    FavoriteListView,
    MyPost,
)

from users.views import (
    PaymentView,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'like', LikeCreateView)
router.register(r'favorite', FavoriteCreateView)
router.register(r'favlist', FavoriteListView)
router.register(r'mypost', MyPost)
router.register(r'payment', PaymentView)

urlpatterns = [
    path('', include(router.urls)),
]
