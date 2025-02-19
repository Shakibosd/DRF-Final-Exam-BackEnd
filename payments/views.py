from django.contrib import messages
from django.conf import settings
from django.shortcuts import redirect, get_object_or_404
import uuid
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from flowers.models import Flower
from orders.models import Order
from django.views.decorators.csrf import csrf_exempt

class SSLCommerzFlowerPaymentView(APIView):
    def get(self, request, flower_id, *args, **kwargs):
        # Get the Flower object based on flower_id
        flower = get_object_or_404(Flower, id=flower_id)

        # Generate a unique transaction ID
        transaction_id = str(uuid.uuid4())

        # SSLCommerz payment request data
        sslcommerz_data = {
            'store_id': settings.SSL_COMMERZ['store_id'],
            'store_passwd': settings.SSL_COMMERZ['store_pass'],
            'total_amount': float(flower.price), 
            'currency': 'BDT',
            'tran_id': transaction_id,
            'success_url': f"https://flower-seal-backend.vercel.app/payments/payment_success/",
            'fail_url': f"https://flower-seal-backend.vercel.app/payments/payment_fail/?id={flower.id}",
            'cancel_url': f"https://flower-seal-backend.vercel.app/payments/payment_cancel/?id={flower.id}",
            'cus_name': 'Test User',
            'cus_email': 'test@example.com',
            'cus_phone': '01700000000',
            'cus_add1': 'Dhaka',
            'cus_city': 'Dhaka',
            'cus_country': 'Bangladesh',
            'shipping_method': 'NO',
            'product_name': flower.title,  
            'product_category': flower.category,
            'product_profile': 'general',
        }

        # SSLCommerz API URL (sandbox or live)
        url = 'https://sandbox.sslcommerz.com/gwprocess/v4/api.php' if settings.SSL_COMMERZ['issandbox'] \
            else 'https://securepay.sslcommerz.com/gwprocess/v4/api.php'

        response = requests.post(url, data=sslcommerz_data)

        if response.status_code == 200:
            res_data = response.json()
            if res_data.get('status') == 'SUCCESS':
                # Redirect directly to SSLCommerz Payment Page
                return redirect(res_data['GatewayPageURL'])
            else:
                return Response({'error': 'SSLCommerz payment failed'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': 'Something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@csrf_exempt 
def payment_success(request, *args, **kwargs):
    tran_id = request.POST.get('tran_id', None)

    if tran_id:
        order = Order.objects.filter(status='Pending').first()
        
        if order:
            order.status = 'Completed'
            order.save()
            messages.success(request, "Payment successfully completed!")  

    return redirect(f'https://flower-seal.netlify.app/order_history.html')


@csrf_exempt 
def payment_fail(request, *args, **kwargs):
    flower_id = request.GET.get('id', None)  
    if flower_id:
        return redirect(f'https://flower-seal.netlify.app/flower_details.html?id={flower_id}')
    else:
        return redirect('https://flower-seal.netlify.app/authenticated_user.html')  

@csrf_exempt 
def payment_cancel(request, *args, **kwargs):
    flower_id = request.GET.get('id', None)
    if flower_id:
        return redirect(f'https://flower-seal.netlify.app/flower_details.html?id={flower_id}')
    else:
        return redirect('https://flower-seal.netlify.app/authenticated_user.html')  