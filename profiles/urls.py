from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChangePasswordViewSet
from profiles.views import UserProfileDetail

router = DefaultRouter()
router.register(r'pass_cng', ChangePasswordViewSet, basename='pass_cng')

urlpatterns = [
    path('', include(router.urls)),
    path('user/<int:id>/', UserProfileDetail.as_view(), name='user-detail'),
]