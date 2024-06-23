# creator_platform/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user_authentications.urls')),
    path('api/brand/', include('brand.urls')),
]

