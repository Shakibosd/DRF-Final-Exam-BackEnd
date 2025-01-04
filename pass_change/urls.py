from django.urls import path
from .views import ChangePasswordAPIView

urlpatterns = [
    path('change_password/', ChangePasswordAPIView.as_view(), name='change_password'),
]
