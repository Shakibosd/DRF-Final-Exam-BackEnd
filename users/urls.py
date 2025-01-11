from django.urls import path, include
from .views import UserAPIView, RegisterAPIView, activate, LoginAPIView, LogoutAPIView

urlpatterns = [
    path('user/', UserAPIView.as_view(), name='user'),  
    path('user/<int:pk>/', UserAPIView.as_view(), name='user_id'),  
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('active/<uid64>/<token>/', activate, name='active'),
]