from rest_framework import viewsets
from .serializers import CommentCheckOrderSerializer, FlowerSerializer, CommentsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Flower, Comment
from orders.models import Order
from rest_framework import generics
from flowers.serializers import CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.mail import send_mail
from .serializers import ContactFormSerializer

#eta hocce amar flower gula show kore deka and flower gula details kore deka
class FlowerViewSet(viewsets.ModelViewSet):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer

class FlowerDetail(APIView):
    def get_object(self, pk):
        try:
            return Flower.objects.get(pk=pk)
        except Flower.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        flower = self.get_object(pk)
        serializer = FlowerSerializer(flower)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        flower = self.get_object(pk)
        serializer = FlowerSerializer(flower, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        flower = self.get_object(pk)
        flower.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#eta hocce flower er modde comment kora comment get post edit delete view kora jay
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer

class CommentShowAPIView(generics.ListAPIView):
    serializer_class = CommentsSerializer
    def get_queryset(self):
        postId = self.kwargs["postId"]
        flower = Flower.objects.get(id = postId)
        return Comment.objects.filter(flower = flower)
        
class CommentAPIView(APIView):        
    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            try:
                flowerId = serializer.validated_data['flowerId']   
                names = serializer.validated_data['names']   
                comment = serializer.validated_data['comment']   
                flower = get_object_or_404(Flower, id=flowerId)
                Comment.objects.create(
                    flower=flower,
                    name=names,
                    body=comment,
                )
                return Response({"comment created"}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"comment not created"}, status=status.HTTP_400_BAD_REQUEST)

#ekane check kora hocce user flower by now korese ki jodi by now kore thake tahole flower er modde comment korte parbe
class CommentCheckOrderAPIView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = CommentCheckOrderSerializer(data=request.query_params)
        if serializer.is_valid():
            flowerId = serializer.validated_data['flowerId']
            user = request.user
            flower = get_object_or_404(Flower, id=flowerId)

            order_exists = Order.objects.filter(user=user, flower=flower).exists()

            return Response({"order_exists": order_exists}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#eta hocce jodi kunu user flower buy kore tahole tar mail er modde ekta mail jabe
class ContactFormView(APIView):
    def post(self, request):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            message = serializer.validated_data['message']
            
            subject = f"Contact Form Submission from {name}"
            email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            send_mail(
                subject,
                email_message,
                'your_email@example.com',  
                ['syednazmusshakib94@gmail.com'],  
                fail_silently=False,
            )
            return Response({"message": "Email sent successfully"}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

