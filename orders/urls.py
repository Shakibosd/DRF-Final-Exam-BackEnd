from django.urls import path
from .views import OrderView, OrderAPIView, OrderSummaryAPIView

urlpatterns = [
    path('create_order/', OrderView.as_view(), name='create_order'),
    path('my_orders/', OrderAPIView.as_view(), name='my-orders'),
    path('order_summary/', OrderSummaryAPIView.as_view(), name='order-summary'),
]