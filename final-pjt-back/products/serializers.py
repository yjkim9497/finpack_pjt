from rest_framework import serializers
from .models import Products, Options, JoinList


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = '__all__'
        read_only_fields = ('product',)

class JoinListSerializer(serializers.ModelSerializer):
  class Meta:
    model = JoinList
    fields = ('option_id', 'product_id',)

class JoinSerializer(serializers.ModelSerializer):
  class Meta:
    model = JoinList
    fields = '__all__'
    read_only_fields = ('user',)