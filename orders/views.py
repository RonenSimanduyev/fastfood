from django.shortcuts import render
from .serializers import CategorySerializer,OrdersSerializer,DishSerializer
from .models import Category,Dish,Orders
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter






# Create your views here.

class CategoryView(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer



class DishView(viewsets.ModelViewSet):
    queryset=Dish.objects.all()
    serializer_class=DishSerializer
    filter_backends=[DjangoFilterBackend,SearchFilter]
    filterset_fields=['category','IsGlutenFree','IsVegeterian']
    search_fields = ['^name']


        

class OrdersView(viewsets.ModelViewSet):
    queryset=Orders.objects.all()
    serializer_class=OrdersSerializer




    @api_view(['GET', 'POST'])
    def orders(request):
        if request.method == 'GET':
            data = Orders.objects.all()

            serializer =OrdersSerializer(data, context={'request': request}, many=True)

            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = OrdersSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)(print=('bad 400'))
