from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FlowerViewSet, FlowerDetail, CommentViewSet, CommentAPIView, CommentShowAPIView, CommentCheckOrderAPIView,ContactFormView

router = DefaultRouter()
router.register('flowers', FlowerViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('flowers/<int:pk>/', FlowerDetail.as_view(), name='flower_details'),
    path('comments_api/', CommentAPIView.as_view(), name='comments_api'),
    path('get_comment/<int:postId>/', CommentShowAPIView.as_view(), name='get_comment'),
    path('check_order/',CommentCheckOrderAPIView.as_view(), name='check_order'),
    path('contact/', ContactFormView.as_view(), name='contact-form'),
]
