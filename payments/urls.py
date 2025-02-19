from django.urls import path
from .views import SSLCommerzFlowerPaymentView
from payments import views
urlpatterns = [
    path('payment/flower/<int:flower_id>/', SSLCommerzFlowerPaymentView.as_view(), name='sslcommerz_payment'),

    path('payment_success/', views.payment_success, name='payment_success'),

    path('payment_fail/', views.payment_fail, name='payment_fail'),

    path('payment_cancel/', views.payment_cancel, name='payment_cancel'),
]
