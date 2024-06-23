# views.py

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Brand, SubscriptionPlan
from .serializers import BrandRegistrationSerializer, BrandLoginSerializer, SubscriptionPlanSerializer
from rest_framework import viewsets
from django.shortcuts import render

class SubscriptionPlanViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer

class BrandRegistrationView(generics.CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandRegistrationSerializer

class BrandLoginView(generics.CreateAPIView):
    serializer_class = BrandLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
