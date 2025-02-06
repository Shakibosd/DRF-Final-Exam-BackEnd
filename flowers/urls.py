from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FlowerViewSet, FlowerDetail, CommentViewSet, CommentAPIView, CommentShowAPIView, CommentCheckOrderAPIView,ContactFormView, FlowerCareTipViewSet, CommentEditAPIView, CartApiView

router = DefaultRouter()
router.register('flowers', FlowerViewSet, basename='flowers')
router.register('comments', CommentViewSet, basename='comments')
router.register('care-tips', FlowerCareTipViewSet, basename='care-tips')


urlpatterns = [
    path('', include(router.urls)),
    path('flowers/', FlowerDetail.as_view(), name='flower_details'),
    path('flowers/<int:pk>/', FlowerDetail.as_view(), name='flower_details'),
    path('comments_api/', CommentAPIView.as_view(), name='comments_api'),
    path('comments_api/<int:commentId>/', CommentAPIView.as_view(), name='comments_api'),
    path('get_comment/<int:postId>/', CommentShowAPIView.as_view(), name='get_comment'),
    path('check_order/', CommentCheckOrderAPIView.as_view(), name='check_order'),
    path('contact/', ContactFormView.as_view(), name='contact-form'),
    path('comments/edit/<int:commentId>/', CommentEditAPIView.as_view(), name='comment-edit'),
    path('cart/', CartApiView.as_view(), name='cart'),
    path('cart/<int:cart_id>/', CartApiView.as_view(), name='cart_remove'),
]