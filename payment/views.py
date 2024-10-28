from sslcommerz_lib import SSLCOMMERZ 
import random, string
from django.http import HttpResponse, HttpResponseRedirect
from flowers.models import Flower

def unique_transaction_id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def payment(request):
    settings = { 'store_id': 'phitr671e3dcf89e2c', 'store_pass': 'phitr671e3dcf89e2c@ssl', 'issandbox': True }
        
    sslcz = SSLCOMMERZ(settings)
    
    post_body = {}
    post_body['total_amount'] = Flower.price #এখানে ওরা ডামি একটা পেমেন্ট দিছে, কিন্তু আমার প্রোডাক্ট এর প্রাইস যত টাকা টিক তত টাকা পেমেন্ট দিবে হবে ইউজার কে।
    post_body['currency'] = "BDT"
    post_body['tran_id'] = unique_transaction_id_generator(),
    post_body['success_url'] = "http://127.0.0.1:8000/orders/my_orders/"
    post_body['fail_url'] = "http://127.0.0.1:8000/orders/my_orders/"
    post_body['cancel_url'] = "http://127.0.0.1:8000/flowers/flowers/"
    post_body['emi_option'] = 0
    post_body['cus_name'] = request.user.username #যে ইউজার প্রোডাক্ট টি কিনবে তার নাম এখানে সো হবে। 
    post_body['cus_email'] = request.user.email #যে ইউজার পোডাক্ট টি কিনবে তার ইমেইল এখানে সো হবে। 
    post_body['cus_phone'] = "01700000000"#যে ইউজার পোডাক্ট টি কিনবে তার মোবাইল এখানে সো হবে। 
    post_body['cus_add1'] = "Cantonment"#যে ইউজার পোডাক্ট টি কিনবে তার ঠিকানা এখানে সো হবে।
    post_body['cus_city'] = "Dhaka"#যে ইউজার পোডাক্ট টি কিনবে তার সিটি এখানে সো হবে।
    post_body['cus_country'] = "Bangladesh"#যে ইউজার পোডাক্ট টি কিনবে তার দেশ এখানে সো হবে।
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = Flower.title
    post_body['product_category'] = Flower.category
    post_body['product_profile'] = "general"


    response = sslcz.createSession(post_body) # API response
    # print(response)
    if response['status'] == 'SUCCESS':
        return HttpResponseRedirect(response['GatewayPageURL'])
    else:
        return HttpResponse("Payment initiation failed. Please try again later.")
    # Need to redirect user to response['GatewayPageURL']