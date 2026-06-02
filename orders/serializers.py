from rest_framework import serializers
from .models import Order, Transaction

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Order
        fields = ['id', 'product', 'account', 'amount', 'status', 'created']
        read_only_fields = ['id', 'status', 'created']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Transaction
        fields = ['id', 'order', 'amount', 'created']