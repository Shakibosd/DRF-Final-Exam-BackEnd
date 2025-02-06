from sslcommerz_lib import SSLCOMMERZ
from django.shortcuts import redirect, get_object_or_404
import random
import string
from flowers.models import Flower
from django.contrib.auth.decorators import login_required

def unique_transaction_id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@login_required
def payments(request, flower_id):
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
        'success_url': "fgd",
        'fail_url': "try",
        'cancel_url': "mnv",
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