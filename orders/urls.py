from django.urls import path
from .views import OrderView, OrderAPIView, AllUsersOrderHistoryAPIView

urlpatterns = [
    path('create_order/', OrderView.as_view(), name='create-order'),
    path('my_order/', OrderAPIView.as_view(), name='my-orders'),
    path('all_order/', AllUsersOrderHistoryAPIView.as_view(), name='all-order'),
]