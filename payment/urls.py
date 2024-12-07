from django.urls import path
from payment import views

urlpatterns = [
    path('payment/<int:flower_id>/', views.payment, name='payment'),
]
