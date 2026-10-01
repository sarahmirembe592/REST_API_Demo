# import serializers from rest_framework
from rest_framework import serializers
# import Product model from models.py
from .models import Product

# create ProductSerializer class
class ProductSerializer(serializers.ModelSerializer):
    # class Meta to specify model and fields
    class Meta:
        model = Product
        fields = '__all__'