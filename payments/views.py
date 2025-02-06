from sslcommerz_lib import SSLCOMMERZ
from django.shortcuts import redirect
import random
import string
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

def unique_transaction_id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@login_required
def payments(request):
    user = request.user  

    settings = { 
        'store_id': 'phitr671e3dcf89e2c', 
        'store_pass': 'phitr671e3dcf89e2c@ssl', 
        'issandbox': True 
    } 

    sslcz = SSLCOMMERZ(settings)
    
    post_body = {
        'total_amount': "100", 
        'currency': "BDT",
        'tran_id': unique_transaction_id_generator(),
        'success_url': "",  
        'fail_url': "",
        'cancel_url': "",
        'emi_option': 0,
        'cus_name': user.username,
        'cus_email': "useremail",
        'cus_phone': "01700000000",  
        'cus_add1': "Cantonment",
        'cus_city': "Dhaka",
        'cus_country': "Bangladesh",
        'shipping_method': "NO",
        'multi_card_name': "demo",
        'num_of_item': 1,
        'product_name': "Rose Flower",  
        'product_category': "Flowers", 
        'product_profile': "general",
    }

    response = sslcz.createSession(post_body)

    if 'GatewayPageURL' in response:
        return redirect(response['GatewayPageURL'])

