from django.urls import path
from .views import registration_view, login_view, SocialMediaHandleListCreateView, SocialMediaHandleDetailView, UserContentDetailListCreateView, UserContentDetailDetailView, UserStoryListCreateView, UserStoryDetailView, DealListCreateView, DealDetailView, RecommendationListView


urlpatterns = [
    path('registration/', registration_view, name='registration'),
    path('login/', login_view, name='login'),
    # Social Media Handles
    path('social-handles/', SocialMediaHandleListCreateView.as_view(), name='social_handles'),
    path('social-handles/<int:pk>/', SocialMediaHandleDetailView.as_view(), name='social_handle_detail'),
    
    # User Content Details
    path('content-details/', UserContentDetailListCreateView.as_view(), name='content_details'),
    path('content-details/<int:pk>/', UserContentDetailDetailView.as_view(), name='content_detail'),
    
    # User Stories
    path('user-stories/', UserStoryListCreateView.as_view(), name='user_stories'),
    path('user-stories/<int:pk>/', UserStoryDetailView.as_view(), name='user_story_detail'),
    
    # Deals
    path('deals/', DealListCreateView.as_view(), name='deals'),
    path('deals/<int:pk>/', DealDetailView.as_view(), name='deal_detail'),
    
    # Recommendations
    path('recommendations/', RecommendationListView.as_view(), name='recommendations'),
]
