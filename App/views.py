from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from .models import Transaction
from .serializers import TransactionSerializer
from django.shortcuts import render


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def logout_view(request):
    logout(request)
    return Response({"message": "Logged out successfully"})

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def credit_view(request):
    amount = request.data.get('amount')
    description = request.data.get('description')
    date = request.data.get('date')
    user = request.user
    transaction = Transaction.objects.create(
        user=user,
        amount=amount,
        description=description,
        date=date,
        credit=amount
    )
    return Response({"message": "Transaction created successfully"})

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def debit_view(request):
    amount = request.data.get('amount')
    description = request.data.get('description')
    date = request.data.get('date')
    user = request.user
    transaction = Transaction.objects.create(
        user=user,
        amount=amount,
        description=description,
        date=date,
        debit=amount
    )
    return Response({"message": "Transaction created successfully"})

class TransactionDeleteView(generics.DestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

def index(request):
    return render(request, 'index.html', {
        'user': request.user,
        'balance': 0.0,
        'transactions': []
    })
    
class TransactionCreateView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
def home(request):
    transactions = Transaction.objects.all()
    balance = 0
    for transaction in transactions:
        if transaction.debit:
            balance -= transaction.amount
        else:
            balance += transaction.amount
    return render(request, 'index.html', {'transactions': transactions, 'balance': balance})
class TransactionList(APIView):

    def post(self, request, format=None):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    