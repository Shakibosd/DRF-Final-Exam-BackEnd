from django.urls import path
from .views import IsAdminView

urlpatterns = [
    path('is_admin/', IsAdminView.as_view(), name='is_admin'),
]