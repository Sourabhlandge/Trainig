from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from account.serializers import UserSerializer
# Create your views here.

class GetServerDetails(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request):
        qs = ServerInventory.objects.filter(os_type="linux Ubantu")
       # qs = ServerInventory.objects.all()
        ser = ServerDetailsSerializer(qs, many=True)
        return Response(ser.data)
        # d = {
        #     'results':'First API'
        # }
        # return Response(d)

class GetServer(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        qs = ServerInventory.objects.filter(os_type="linux Ubantu")
       # qs = ServerInventory.objects.all()
        ser = ServerDetailsSerializer(qs, many=True)
        return Response(ser.data)

# class SignupAPI(APIView):
#     def post(self, request):
#         print("Request=", request.data)
#         ser = UserSerializer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#         return Response(ser.data, status=status.HTTP_201_CREATED)   