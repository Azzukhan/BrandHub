from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from .models import SocialMediaHandle, UserContentDetail, UserStory, Deal, Recommendation


User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'password', 'password2')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid login credentials.")
        data['user'] = user
        return data


class SocialMediaHandleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaHandle
        fields = ['id', 'platform', 'handle', 'followers']

class UserContentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContentDetail
        fields = ['id', 'content_type', 'highest_view_count', 'highest_view_video']

class UserStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStory
        fields = ['id', 'story', 'biggest_deal', 'achievements', 'available_time_for_interview', 'address']

class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = ['id', 'title', 'description', 'creator', 'applied', 'status']

class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = ['id', 'user', 'deal']
