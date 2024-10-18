from django.urls import path
from .views import OrderView, OrderAPIView

urlpatterns = [
    path('create_order/', OrderView.as_view(), name='create_order'),
    path('my_orders/', OrderAPIView.as_view(), name='my-orders'),
]