from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from orders.models import Order
from django.db.models import Sum, F
from decimal import Decimal

#ei code diye check kortesi user admin super user ki na.
class IsAdminView(APIView): 
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.is_staff:  
            return Response({"is_admin": True})
        return Response({"is_admin": False})


class OrderStatsAPIView(APIView):
    def get(self, request):
        total_orders = Order.objects.count()  
        total_products = Order.objects.aggregate(total_products=Sum('quantity'))['total_products'] or 0 
         
        total_revenue = Order.objects.annotate(
        total_price=F('quantity') * F('flower__price')
        ).aggregate(total_revenue=Sum('total_price'))['total_revenue'] or Decimal('0')

        profit = total_revenue * Decimal('0.10')  
        
        return Response({
            "total_orders": total_orders,
            "total_revenue": float(total_revenue),
            "total_products": total_products,
            "profit": float(profit),
        })