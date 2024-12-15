from sslcommerz_lib import SSLCOMMERZ
from django.shortcuts import get_object_or_404, redirect
from flowers.models import Flower
import random
import string

def unique_transaction_id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def payment(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id)

    settings = { 
        'store_id': 'phitr671e3dcf89e2c', 
        'store_pass': 'phitr671e3dcf89e2c@ssl', 
        'issandbox': True 
    }
    
    sslcz = SSLCOMMERZ(settings)
    
    post_body = {
        'total_amount': flower.price,  
        'currency': "BDT",
        'tran_id': unique_transaction_id_generator(),
        'success_url': f"https://flower-seal.netlify.app/flower_details.html?id={flower.id}",
        'fail_url': f"https://flower-seal.netlify.app/flower_details.html?id={flower.id}",
        'cancel_url': f"https://flower-seal.netlify.app/flower_details.html?id={flower.id}",
        'emi_option': 0,
        'cus_name': "request.user.username",  # Dynamically get user info
        'cus_email':" request.user.email",
        'cus_phone': "request.user.profile.phone",  # Assuming user has profile with phone field
        'cus_add1': "Cantonment",
        'cus_city': "Dhaka",
        'cus_country': "Bangladesh",
        'shipping_method': "NO",
        'multi_card_name': "demo",
        'num_of_item': 1,
        'product_name': flower.title,
        'product_category': flower.category,
        'product_profile': "general"
    }

    response = sslcz.createSession(post_body)
    
    if response['status'] == 'SUCCESS':
        return redirect(response['GatewayPageURL'])
    else:
        # Handle failure, e.g., log error or notify user
        return redirect('failure_url')  # You may define a failure URL or message
