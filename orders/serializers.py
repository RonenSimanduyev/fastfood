from django.forms import SlugField
from rest_framework import serializers
from .models import Category,Dish,Orders

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = ('id','name','imageUrl')



class DishSerializer(serializers.ModelSerializer):   
    class Meta:
        model=Dish
        fields='category','id','name','price','description','imageUrl','IsGlutenFree','IsVegeterian'


    def to_representation(self,instance):
        data1=super().to_representation(instance)
        data1['category.id']=CategorySerializer(instance.category).data

        return data1


class OrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model=Orders
        fields='__all__'

    def to_representation(self,instance):
        data=super().to_representation(instance)
        data['dishes']=DishSerializer(instance.dishes,many=True).data

        return data



