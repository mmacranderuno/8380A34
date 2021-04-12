from rest_framework import serializers
from .models import Customer, Investment, Stock


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('pk', 'name', 'cust_number', 'address', 'city', 'state', 'zipcode', 'email', 'email', 'cell_phone',
                  'custdisplay')


class InvestmentSerializer(serializers.ModelSerializer):
    custdisplay = serializers.CharField(source='customer.custdisplay', required=False, read_only=True)

    class Meta:
        model = Investment
        fields = ('pk', 'customer', 'category', 'description', 'acquired_value', 'acquired_date', 'recent_value',
                  'recent_date', 'custdisplay',)


class StockSerializer(serializers.ModelSerializer):
    custdisplay = serializers.CharField(source='customer.custdisplay', required=False, read_only=True)

    class Meta:
        model = Stock
        fields = ('pk', 'customer', 'symbol', 'name', 'shares', 'purchase_price', 'purchase_date', 'custdisplay',)
