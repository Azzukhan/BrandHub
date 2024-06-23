from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework import generics
from .models import SocialMediaHandle, UserContentDetail, UserStory , Deal, Recommendation
from .serializers import SocialMediaHandleSerializer, UserContentDetailSerializer, UserStorySerializer , DealSerializer, RecommendationSerializer
from rest_framework.permissions import IsAuthenticated




class SocialMediaHandleListCreateView(generics.ListCreateAPIView):
    serializer_class = SocialMediaHandleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SocialMediaHandle.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SocialMediaHandleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SocialMediaHandleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SocialMediaHandle.objects.filter(user=self.request.user)
    

class UserContentDetailListCreateView(generics.ListCreateAPIView):
    serializer_class = UserContentDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserContentDetail.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserContentDetailDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserContentDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserContentDetail.objects.filter(user=self.request.user)

class UserStoryListCreateView(generics.ListCreateAPIView):
    serializer_class = UserStorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserStory.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserStoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserStorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserStory.objects.filter(user=self.request.user)

# Deals
class DealListCreateView(generics.ListCreateAPIView):
    serializer_class = DealSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Deal.objects.filter(creator=self.request.user)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class DealDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DealSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Deal.objects.filter(creator=self.request.user)

# Recommendations
class RecommendationListView(generics.ListAPIView):
    serializer_class = RecommendationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Recommendation.objects.filter(user=self.request.user)

User = get_user_model()

@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
