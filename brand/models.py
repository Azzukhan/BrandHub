# models.py

from django.db import models

class SubscriptionPlan(models.Model):
    PLAN_CHOICES = [
        ('basic', 'Basic'),
        ('advanced', 'Advanced'),
        ('premium', 'Premium')
    ]
    name = models.CharField(max_length=50, choices=PLAN_CHOICES, unique=True)
    post_limit = models.IntegerField(default=0)  # 0 for unlimited
    creator_limit = models.IntegerField(default=0)  # 0 for unlimited

    def __str__(self):
        return self.name

class Brand(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    position_in_company = models.CharField(max_length=100)
    person_name = models.CharField(max_length=100)
    company_mail_id = models.EmailField(unique=True)
    company_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    subscription_type = models.ForeignKey(SubscriptionPlan, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username
