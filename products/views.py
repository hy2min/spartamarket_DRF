
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
    def post(self,request) :
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
