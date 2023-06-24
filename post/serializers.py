from rest_framework import serializers
from .models import Post


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

