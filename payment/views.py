from sslcommerz_lib import SSLCOMMERZ
import random, string
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.conf import settings

def unique_transaction_id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class PaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # SSLCommerz settings
        sslcommerz_settings = {
            'store_id': 'phitr671e3dcf89e2c',
            'store_pass': 'phitr671e3dcf89e2c@ssl',
            'issandbox': True
        }
        
        sslcz = SSLCOMMERZ(sslcommerz_settings)
        
        # Post data
        post_body = {
            'total_amount': 100.26, # এখানে ফ্লাওয়ারের প্রাইস ডাইনামিকলি সেট করতে হবে।
            'currency': "BDT",
            'tran_id': unique_transaction_id_generator(),
            'success_url': "https://flower-seal.netlify.app/update_profile.html",
            'fail_url': "https://flower-seal.netlify.app/update_profile.html",
            'cancel_url': "https://flower-seal.netlify.app/profile.html",
            'emi_option': 0,
            'cus_name': request.user.username, 
            'cus_email': request.user.email,
            'cus_phone':  "01700000000", 
            'cus_add1': "Cantonment",
            'cus_city': "Dhaka", 
            'cus_country': "Bangladesh",
            'shipping_method': "NO",
            'multi_card_name': "",
            'num_of_item': 1,
            'product_name': "Test",
            'product_category': "Test Category",
            'product_profile': "general"
        }

        # Create payment session
        response = sslcz.createSession(post_body)
        
        if response['status'] == 'SUCCESS':
            return HttpResponseRedirect(response['GatewayPageURL'])
        else:
            return HttpResponse("Payment initiation failed. Please try again later.")
