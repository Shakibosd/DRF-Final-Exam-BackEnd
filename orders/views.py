from venv import logger
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Order
from flowers.models import Flower
from .serializers import OrderSerializer, OrderCreateSerializer, OrderSerializerForCreate
from .constants import PENDING, COMPLETED
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Order
from .serializers import OrderSerializer
from django.db import models

#eta hocce flower order korar jonno post and get
class OrderAPIView(APIView): 
    def get(self, request, *args, **kwargs):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = OrderCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#eta hocce order history dekar jonno and order view dekar jonno and flower kinar pore email jabe and flower buy korle quentity kome jabe
class OrderView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = OrderSerializerForCreate(data=request.data)
        if serializer.is_valid():
            user = request.user
            product_id = serializer.validated_data['product_id']
            quantity = serializer.validated_data['quantity']
            flower = get_object_or_404(Flower, id=product_id)

            if flower.stock < quantity:
                return Response({'error': 'Insufficient stock available'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                order = Order.objects.create(
                    user=user,
                    flower=flower,
                    quantity=quantity,
                    status='Pending',
                )
                flower.stock -= quantity
                flower.save()

                # Sending email
                email_subject = 'Order Confirmation'
                email_body = render_to_string('order_confirmation_email.html', {
                    'user': user,
                    'flower': flower,
                    'quantity': quantity,
                    'order': order,
                })
                email = EmailMultiAlternatives(email_subject, '', to=[user.email])
                email.attach_alternative(email_body, 'text/html')
                email.send()

                return Response({'status': 'Order Placed Successfully. Check Your Email'}, status=status.HTTP_201_CREATED)
            except Exception as e:
                logger.error(f"Error creating order or sending email: {e}")
                return Response({'error': 'Order creation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'error': 'Invalid data', 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class OrderSummaryAPIView(APIView):
    def get(self, request, *args, **kwargs):
        total_products_sold = Order.objects.aggregate(total_quantity=models.Sum('quantity'))['total_quantity'] or 0
        total_revenue = Order.objects.aggregate(total_revenue=models.Sum('revenue'))['total_revenue'] or 0.0
        total_profit = Order.objects.aggregate(total_profit=models.Sum('profit'))['total_profit'] or 0.0
        
        return Response({
            'total_products_sold': total_products_sold,
            'total_revenue': total_revenue,
            'total_profit': total_profit
        })


class AllUsersOrderHistoryAPIView(APIView):
    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
