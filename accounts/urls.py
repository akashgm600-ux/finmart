from django.urls import path
from .views import BankAccountListCreateView, BankAccountDetailView

urlpatterns = [
    path('', BankAccountListCreateView.as_view(), name='account-list'),
    path('<int:pk>/', BankAccountDetailView.as_view(), name='account-detail'),
]