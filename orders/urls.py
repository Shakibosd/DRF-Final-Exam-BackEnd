from django.urls import path
from .views import OrderView, OrderAPIView, OrderSummaryAPIView, AllUsersOrderHistoryAPIView

urlpatterns = [
    path('create_order/', OrderView.as_view(), name='create-order'),
    path('my_orders/', OrderAPIView.as_view(), name='my-orders'),
    path('order_summary/', OrderSummaryAPIView.as_view(), name='order-summary'),
    path('all_orders/', AllUsersOrderHistoryAPIView.as_view(), name='all-order'),
]