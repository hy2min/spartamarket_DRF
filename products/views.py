
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

class ProductListAPIView(APIView) :
    def get(self,request) :
        products = Product.objects.all()
        serializers = ProductSerializer(products,many=True)
        json_response = serializers.data
        return Response(json_response)
