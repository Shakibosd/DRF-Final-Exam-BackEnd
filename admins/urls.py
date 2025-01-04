from django.urls import path
from django.urls import path
from .views import OrderStatsAPIView
from django.urls import path
from .views import IsAdminView

urlpatterns = [
    path('is_admin/', IsAdminView.as_view(), name='is_admin'),
    path('order-stats/', OrderStatsAPIView.as_view(), name='order_stats'),
]