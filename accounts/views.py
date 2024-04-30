from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import AccountSerializer

class AccountCreateAPIView(APIView) :
    def post(self,request) :
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
class AccountDetailAPIView(APIView) :
    def get(self,request,username) :
        account = get_object_or_404(User,username = username)
        serializer = AccountSerializer(account)
        return Response(serializer.data)        