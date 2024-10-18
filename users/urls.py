from django.urls import path, include
from .views import UserViewSet, RegisterAPIView, activate, LoginAPIView, LogoutAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('active/<uid64>/<token>/', activate, name='active'),
]