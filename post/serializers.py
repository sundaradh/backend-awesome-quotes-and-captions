from rest_framework import serializers
from .models import Like, Post, Favorite


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.full_name')
    likes = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    date_posted = serializers.SerializerMethodField()
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['id', 'user', 'author', 'likes',
                            'category_name', 'date_posted', 'is_liked', 'is_favorite']

    def get_likes(self, obj):
        return obj.likes.count()

    def get_category_name(self, obj):
        return obj.category.name

    def get_is_liked(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return Like.objects.filter(user=user, post=obj).exists()
        return False

    def get_is_favorite(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return Favorite.objects.filter(user=user, post=obj).exists()
        return False

    def get_date_posted(self, obj):
        return obj.date_posted.strftime('%d %b %Y')

    def create(self, validated_data):
        validated_data['is_active'] = True
        return super().create(validated_data)


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'post', 'user')
        read_only_fields = ['id', 'user']

    def create(self, validated_data):
        user = self.context['request'].user
        # update likes on post model
        post = validated_data['post']

        if Like.objects.filter(user=user, post=post).exists():
            Like.objects.filter(user=user, post=post).delete()
            post.likes.remove(user)
            raise serializers.ValidationError('This post is already liked.')

        else:
            post.likes.add(user)
            return super().create(validated_data)


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'post', 'user')
        read_only_fields = ['id', 'user']

    def create(self, validated_data):
        user = self.context['request'].user
        post = validated_data['post']

        if existing_favorite := Favorite.objects.filter(
                user=user, post=post
        ).first():
            # Remove the existing favorite if found
            existing_favorite.delete()
            print("Post removed from favorites.")
            raise serializers.ValidationError('Post removed from favorites.')
        else:
            # Create a new favorite if not found
            favorite = super().create(validated_data)
            print("Post added to favorites.")
            return favorite


class FavListSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()
    date_posted = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    is_favorite = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()


    class Meta:
        model = Favorite
        fields = ['post', 'category_name', 'author', 'date_posted', 'is_liked', 'is_favorite', 'likes']
        depth = 1

    def get_category_name(self, obj):
        return obj.post.category.name

    def get_author(self, obj):
        return obj.post.author.full_name

    def get_date_posted(self, obj):
        return obj.post.date_posted.strftime('%d %b %Y')

    def get_is_liked(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return Like.objects.filter(user=user, post=obj.post).exists()
        return False

    def get_is_favorite(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return Favorite.objects.filter(user=user, post=obj.post).exists()
        return False
    def get_likes(self, obj):
        return obj.post.likes.count()