from ast import Delete
from email.mime import image
from pickle import TRUE
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    imageUrl=models.CharField(max_length=1000,blank=True)

    def __str__(self) :
        return (self.name)

class Dish(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE, related_name='category')
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.TextField()
    imageUrl=models.CharField(max_length=1000)
    IsGlutenFree=models.BooleanField(default=False)
    IsVegeterian=models.BooleanField(default=False)
    
    def __str__(self) :
        return (self.name)


class Orders(models.Model):
    dishes = models.ManyToManyField(Dish)
    time=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    def __str__(self) :
        return (self.dishes)
