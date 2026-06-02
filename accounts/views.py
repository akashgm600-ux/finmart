from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import BankAccount
from .serializers import BankAccountSerializer

class BankAccountListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        accounts = BankAccount.objects.filter(user=request.user)
        serializer = BankAccountSerializer(accounts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BankAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BankAccountDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return BankAccount.objects.get(pk=pk, user=user)
        except BankAccount.DoesNotExist:
            return None

    def get(self, request, pk):
        account = self.get_object(pk, request.user)
        if not account:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(BankAccountSerializer(account).data)

    def delete(self, request, pk):
        account = self.get_object(pk, request.user)
        if not account:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        account.delete()
        return Response({'message': 'Account deleted'}, status=status.HTTP_204_NO_CONTENT)