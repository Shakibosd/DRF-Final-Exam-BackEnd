from django.urls import path
from payments import views

urlpatterns = [
    path('payments/<int:flower_id>/', views.payments, name='payments'),
]