from rest_framework import serializers
from django.contrib.auth import get_user_model

from users.models import Payment

# create serializers for users
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'address', 'mobile','is_subscriber']


class PayementSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    class Meta:
        model = Payment
        fields = ['payment_method', 'amount', 'payment_status', 'created_at' ]
        read_only_fields = ['created_at']

    def get_created_at(self, obj):
        return obj.created_at.strftime('%d %b %Y')
