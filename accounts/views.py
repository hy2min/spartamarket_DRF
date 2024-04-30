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