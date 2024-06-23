# myapp/middleware.py

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.urls import reverse

class SubscriptionLimitMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if not request.user.is_authenticated:
            return None

        user = request.user
        if hasattr(user, 'subscription_type') and user.subscription_type:
            # Check post limits for the Basic package
            if user.subscription_type.name == 'basic' and user.post_set.count() >= user.subscription_type.post_limit:
                return redirect(reverse('upgrade_package'))
            # Check creator limits for the Basic package
            if user.subscription_type.name == 'basic' and user.creator_set.count() >= user.subscription_type.creator_limit:
                return redirect(reverse('upgrade_package'))

        return None
