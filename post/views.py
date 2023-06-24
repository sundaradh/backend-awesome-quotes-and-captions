from requests import Response
from rest_framework import authentication, permissions, viewsets
from .models import Post, Like, Favorite
from .serializers import PostSerializer, LikeSerializer, FavoriteSerializer, FavListSerializer


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


class LikeCreateView(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MyPost(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class FavoriteCreateView(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    def get_queryset(self):
        queryset = Favorite.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavoriteListView(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavListSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)
