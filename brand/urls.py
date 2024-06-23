# brand/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BrandRegistrationView, BrandLoginView, SubscriptionPlanViewSet

router = DefaultRouter()
router.register(r'subscription-plans', SubscriptionPlanViewSet, basename='subscriptionplan')

urlpatterns = [
    path('register/', BrandRegistrationView.as_view(), name='brand_register'),
    path('login/', BrandLoginView.as_view(), name='brand_login'),
    path('', include(router.urls)),
]
