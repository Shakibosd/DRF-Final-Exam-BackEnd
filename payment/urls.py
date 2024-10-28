from django.urls import path
from payment import views

urlpatterns = [
    path('payment/', views.PaymentView.as_view(), name='payment'),
]
