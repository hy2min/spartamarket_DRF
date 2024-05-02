from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated, 
    IsAuthenticatedOrReadOnly
)
from .models import User
from .serializers import AccountSerializer, AccountDetailSerializer

class AccountCreateAPIView(APIView) :
    def post(self,request) :
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
class AccountDetailAPIView(APIView) :
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request,username) :
        account = get_object_or_404(User,username = username)
        serializer = AccountDetailSerializer(account)
        return Response(serializer.data)
    def put(self,request,username) :
        account = get_object_or_404(User,username = username)
        if account.id == request.user.id :
            serializer = AccountDetailSerializer(account, data=request.data, partial = True)
            if serializer.is_valid(raise_exception=True) :
                serializer.save()
                return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
