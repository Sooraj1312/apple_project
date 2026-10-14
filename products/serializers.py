from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    category=serializers.ReadOnlyField(source='category.name')
    
    class Meta:
        modeel= Product
        fields= '__all__'