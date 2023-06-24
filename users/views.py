from django.shortcuts import render
from rest_framework import viewsets, permissions
from users.models import (
    User,
    Payment,
)
from users.serializers import (
    UserSerializer,
    PayementSerializer,
)


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentView(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PayementSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        user.is_subscriber = True
        user.save()
        serializer.save(user=user)
