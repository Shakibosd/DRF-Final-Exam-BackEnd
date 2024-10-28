from django.urls import path
from payment import views

urlpatterns = [
    path('payment/', views.payment, name='payment'),
]
