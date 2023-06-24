from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    class Meta:
        model = Notification
        fields = '__all__'
        read_only_fields = ['id', 'user']
        depth = 1

    def get_created_at(self, obj):
        return obj.created_at.strftime('%d %b %Y')

    def get_updated_at(self, obj):
        return obj.updated_at.strftime('%d %b %Y')