from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from .helpers import custom_response
from rest_framework import status
from drf_spectacular.utils import extend_schema

# Create your views here.


class ItemView(APIView):
    serializer_class = ItemSerializer
   
    def get(self,request):
        db_items = Item.objects.all()
        try:
            serializer_items = ItemSerializer(db_items, many=True)
            return custom_response(serializer_items.data,"successfull",status.HTTP_200_OK)
        except Exception as Error:
            return custom_response(str(Error),"Unsucessfull",status.HTTP_500_INTERNAL_SERVER_ERROR)
    @extend_schema(
        request=ItemSerializer,
        responses={
            status.HTTP_201_CREATED: {
                                        "example": [
                                            {
                                            "item_id": 1,
                                            "name": "Iphone15",
                                            "price": "100000.00",
                                            'quantity':'0',
                                            "description": "Mobile of apple company 256GB rom ,16GB ram"
                                            },
                                            {
                                            "item_id": 2,
                                            "name": "MI",
                                            "price": "10000.00",
                                            'quantity':'0',
                                            "description": ""
                                            }
                                        ],
                                        "message": "successfull"
                                        },
            status.HTTP_400_BAD_REQUEST: {"example": {"error": "Bad request"}}
        }
    )   
    def post(self, request):
        try:
            serializer = ItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return custom_response(serializer.data, "successfull",status.HTTP_200_OK)
        except Exception as Error:
            return custom_response(str(Error), "Unsuccessfull",status.HTTP_500_INTERNAL_SERVER_ERROR)
        


