from django.http import JsonResponse
from sslcommerz_lib import SSLCOMMERZ
from django.shortcuts import get_object_or_404, redirect
from flowers.models import Flower
from orders.models import Order
import random
import string
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

def unique_transaction_id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def payment(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id)

    settings = { 
        'store_id': 'phitr671e3dcf89e2c', 
        'store_pass': 'phitr671e3dcf89e2c@ssl', 
        'issandbox': True 
    }
    user = request.user  

    cus_name = user.username
    cus_email = user.email  

    sslcz = SSLCOMMERZ(settings)
    
    post_body = {
        'total_amount': flower.price,  
        'currency': "BDT",
        'tran_id': unique_transaction_id_generator(),
        'success_url': f"http://127.0.0.1:8000/payment/payment_success/",
        'fail_url': f"http://127.0.0.1:8000/payment/payment_fail/?id={flower.id}",
        'cancel_url': f"http://127.0.0.1:8000/payment/payment_cancel/?id={flower.id}",
        'emi_option': 0,
        'cus_name': cus_name,
        'cus_email': cus_email,
        'cus_phone': "01700000000",
        'cus_add1': "Cantonment",
        'cus_city': "Dhaka",
        'cus_country': "Bangladesh",
        'shipping_method': "NO",
        'multi_card_name': "demo",
        'num_of_item': 1,
        'product_name': flower.title,
        'product_category': flower.category,
        'product_profile': "general",
    }

    response = sslcz.createSession(post_body)  
    # print(response)

    return redirect(response['GatewayPageURL'])


@csrf_exempt
def payment_success(request, *args, **kwargs):
    tran_id = request.POST.get('tran_id', None)

    if tran_id:
        order = Order.objects.filter(status='Pending').first()
        
        if order:
            order.status = 'Completed'
            order.save()
        messages.success(request, "Payment successfully completed!")

    return redirect('http://127.0.0.1:5500/update_profile.html')


@csrf_exempt
def payment_fail(request, *args, **kwargs):
    flower_id = request.GET.get('id', None)  
    if flower_id:
        return redirect(f'http://127.0.0.1:5500/flower_details.html?id={flower_id}')
    else:
        return redirect('http://127.0.0.1:5500/profile.html')  

@csrf_exempt
def payment_cancel(request, *args, **kwargs):
    flower_id = request.GET.get('id', None)
    if flower_id:
        return redirect(f'http://127.0.0.1:5500/flower_details.html?id={flower_id}')
    else:
        return redirect('http://127.0.0.1:5500/profile.html')  