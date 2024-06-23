from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken

class CustomUser(AbstractUser):
    is_creator = models.BooleanField(default=True)
    phone = models.CharField(max_length=15)
    email_verified = models.BooleanField(default=False)
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
    )

class OutstandingToken(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='outstanding_tokens'
    )
    jti = models.UUIDField()
    token = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    class Meta:
        unique_together = ('user', 'jti')

class SocialMediaHandle(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='social_media_handles')
    platform = models.CharField(max_length=50)
    handle = models.CharField(max_length=100)
    followers = models.IntegerField()

    def __str__(self):
        return f"{self.platform}: {self.handle}"

class UserContentDetail(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='content_details')
    content_type = models.CharField(max_length=100)
    highest_view_count = models.IntegerField()
    highest_view_video = models.URLField()

    def __str__(self):
        return f"{self.content_type} - {self.highest_view_count}"

class UserStory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='stories')
    story = models.TextField()
    biggest_deal = models.TextField()
    achievements = models.TextField()
    available_time_for_interview = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} - Story"

class Deal(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='deals')
    applied = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return self.title

class Recommendation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='recommendations')
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE, related_name='recommendations')
