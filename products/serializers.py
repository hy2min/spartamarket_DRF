from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Product
        fields = '__all__'
        # read_only_fields = ("account",)
        
    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     ret.pop("account")
    #     return ret