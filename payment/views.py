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
        'success_url': "",
        'fail_url': "",
        'cancel_url': "",
        'emi_option': 0,
        'cus_name': "requestuserusername",
        'cus_email': "requestuseremail",
        'cus_phone': "01700000000",
        'cus_add1': "Cantonment",
        'cus_city': "Dhaka",
        'cus_country': "Bangladesh",
        'shipping_method': "NO",
        'multi_card_name': "",
        'num_of_item': 1,
        'product_name': "flowertitle",
        'product_category': "flowercategory",
        'product_profile': "general"
    }

    response = sslcz.createSession(post_body)  
    print(response)
    
    return redirect(response['GatewayPageURL'])
