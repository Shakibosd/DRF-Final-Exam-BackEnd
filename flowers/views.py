from rest_framework import viewsets
from .serializers import CommentCheckOrderSerializer, FlowerSerializer, CommentsSerializer, CommentEditSerializer, CartItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Flower, Comment, CartItem
from orders.models import Order 
from rest_framework import generics
from flowers.serializers import CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.mail import send_mail
from .serializers import ContactFormSerializer
from .models import PlantRevivalTip
from .serializers import FlowerCareTipSerializer
import logging
logger = logging.getLogger(__name__)

#eta hocce amar flower gula show kore deka and flower gula details kore deka
class FlowerViewSet(viewsets.ModelViewSet):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer


class FlowerDetail(APIView):
    def get_object(self, pk):
        try:
            return Flower.objects.get(pk=pk)
        except Flower.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        flower = self.get_object(pk)
        serializer = FlowerSerializer(flower)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        flower = self.get_object(pk)
        serializer = FlowerSerializer(flower, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        flower = self.get_object(pk)
        flower.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#eta hocce flower er modde comment kora comment get post edit delete view kora jay
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer

class CommentShowAPIView(generics.ListAPIView):
    serializer_class = CommentsSerializer
    def get_queryset(self):
        postId = self.kwargs["postId"]
        flower = Flower.objects.get(id = postId)
        return Comment.objects.filter(flower = flower)
                    
class CommentAPIView(APIView):
    def post(self, request, *args, **kwargs):        
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            try:
                flowerId = serializer.validated_data['flowerId']
                comment = serializer.validated_data['comment']
                flower = get_object_or_404(Flower, id=flowerId)
                
                user = request.user  

                Comment.objects.create(
                    flower=flower,
                    user=user,
                    body=comment,
                )
                return Response({"message": "Comment created successfully!"}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Comment not created"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, commentId):
        try:
            comment = Comment.objects.get(id=commentId)
            comment.delete()
            return Response({"message": "Comment deleted successfully"}, status=status.HTTP_200_OK)
        except Comment.DoesNotExist:
            return Response({"error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)

#ekane check kora hocce user flower by now korese ki jodi by now kore thake tahole flower er modde comment korte parbe

class CommentCheckOrderAPIView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = CommentCheckOrderSerializer(data=request.query_params)
        if serializer.is_valid():
            flowerId = serializer.validated_data['flowerId']
            user = request.user
            flower = get_object_or_404(Flower, id=flowerId)

            # Log user, flower, and query result
            logger.info(f"User: {user}, Flower: {flower}")
            orders = Order.objects.filter(user=user, flower=flower)
            logger.info(f"Orders found: {orders.exists()}")

            order_exists = orders.exists()

            return Response({"order_exists": order_exists}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#eta hocce jodi kunu user flower buy kore tahole tar mail er modde ekta mail jabe
class ContactFormView(APIView):
    def post(self, request):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            message = serializer.validated_data['message']
            
            subject = f"Contact Form Submission from {name}"
            email_message = f"Name : {name}\nEmail : {email}\nMessage : \n{message}"

            try:
                send_mail(
                    subject,
                    email_message,
                    'noreply@yourdomain.com',  
                    ['syednazmusshakib94@gmail.com'],
                    fail_silently=False,
                )
                return Response({"message": "Email sent successfully"}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentEditAPIView(APIView):
    def put(self, request, *args, **kwargs):
        comment_id = self.kwargs['commentId']  
        comment = Comment.objects.get(id=comment_id)

        serializer = CommentEditSerializer(comment, data=request.data, partial=True)   
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Comment updated successfully!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FlowerCareTipViewSet(viewsets.ModelViewSet):
    queryset = PlantRevivalTip.objects.all()
    serializer_class = FlowerCareTipSerializer
    

class CartApiView(APIView):

    def get(self, request, *args, **kwargs):
        cart_items = CartItem.objects.filter(user=request.user)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        flower_id = request.data.get("flower")
        quantity = request.data.get("quantity")

        if not flower_id or not quantity:
            return Response({"error": "Missing flower or quantity data"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            flower = Flower.objects.get(id=flower_id)
        except Flower.DoesNotExist:
            return Response({"error": "Flower not found"}, status=status.HTTP_404_NOT_FOUND)

        existing_item = CartItem.objects.filter(flower=flower, user=request.user).first()
        if existing_item:
            return Response({"error": "This product is already in your cart!"}, status=status.HTTP_400_BAD_REQUEST)

        cart_item = CartItem.objects.create(user=request.user, flower=flower, quantity=quantity)
        return Response({"message": "Product added successfully!", "cart_item": cart_item.id}, status=status.HTTP_201_CREATED)

    def delete(self, request, cart_id, *args, **kwargs):
        try:
            cart_item = CartItem.objects.get(id=cart_id, user=request.user)
            cart_item.delete()
            return Response({"Message" : "Item removed form cart success"}, status=status.HTTP_200_OK)
        
        except CartItem.DoesNotExist:
            return Response({"Error" : "Cart item not found"}, status=status.HTTP_404_NOT_FOUND)