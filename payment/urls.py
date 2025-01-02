from django.urls import path
from payment import views

urlpatterns = [
    path('payment/<int:flower_id>/', views.payment, name='payments'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('payment_fail/', views.payment_fail, name='payment_fail'),
    path('payment_cancel/', views.payment_cancel, name='payment_cancel'),
]
