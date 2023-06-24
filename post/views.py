from rest_framework import authentication, permissions, viewsets
from .models import Post
from .serializers import PostSerializer


# Create your views here.


class IsRewiver(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # lookup_field = 'id'
    permission_classes = [IsRewiver, permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication,
                              authentication.SessionAuthentication]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = Post.objects.filter(
            is_active=True
        )
        if self.request.user.is_authenticated:
            queryset = queryset

        return queryset

