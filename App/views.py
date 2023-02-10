from rest_framework import viewsets
from .models import Transaction
from .serializers import TransactionSerializer
from django.shortcuts import render
from .models import Transaction

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

def index(request):
    return render(request, 'index.html', {
        'user': request.user,
        'balance': 0.0,
        'transactions': []
    })

def home(request):
    transactions = Transaction.objects.all()
    balance = 0
    for transaction in transactions:
        if transaction.debit:
            balance -= transaction.amount
        else:
            balance += transaction.amount
    return render(request, 'index.html', {'transactions': transactions, 'balance': balance})