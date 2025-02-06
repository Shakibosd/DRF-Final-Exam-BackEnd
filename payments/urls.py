from django.urls import path
from payments import views

urlpatterns = [
    path('payments/', views.payments, name='payments'),
]