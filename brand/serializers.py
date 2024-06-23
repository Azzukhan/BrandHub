# serializers.py

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .models import SubscriptionPlan, Brand

class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = ['name', 'post_limit', 'creator_limit']

class BrandRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Brand
        fields = ['id', 'username', 'password', 'email', 'position_in_company', 'person_name', 'company_mail_id', 'company_name', 'contact_number', 'subscription_type']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        brand = Brand.objects.create(**validated_data)
        return brand

class BrandLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            try:
                brand = Brand.objects.get(email=email)
                if check_password(password, brand.password):  # Compare hashed password
                    refresh = RefreshToken()
                    refresh.access_token.payload['email'] = brand.email
                    refresh.access_token.payload['username'] = brand.username
                    return {
                        'email': brand.email,
                        'username': brand.username,
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    }
                else:
                    raise serializers.ValidationError({'error': 'Invalid credentials'})
            except Brand.DoesNotExist:
                raise serializers.ValidationError({'error': 'Brand with this email does not exist'})
        else:
            raise serializers.ValidationError({'error': 'Email and password are required'})
