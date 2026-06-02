from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Order, Transaction
from .serializers import OrderSerializer, TransactionSerializer

class OrderListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user).select_related('product', 'account')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save(user=request.user)
            Transaction.objects.create(order=order, amount=order.amount)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transactions = Transaction.objects.filter(order__user=request.user)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)