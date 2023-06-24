from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()  
    date_posted = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'
        

   

    def get_category_name(self, obj):
        return obj.category.name

    def get_date_posted(self, obj):
        return obj.date_posted.strftime('%d %b %Y')

    def create(self, validated_data):
        validated_data['is_active'] = True
        return super().create(validated_data)

