from django.urls import path
from .views import OrderListCreateView, TransactionListView

urlpatterns = [
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('transactions/', TransactionListView.as_view(), name='transaction-list'),
]