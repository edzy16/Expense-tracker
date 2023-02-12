from django.urls import path, include
from rest_framework import routers
from .views import TransactionViewSet, home, TransactionDeleteView,TransactionCreateView

router = routers.DefaultRouter()
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('home/', home, name='home'),
    path('delete/<int:pk>/', TransactionDeleteView.as_view(), name='transaction_delete'),
    path('api/transactions/', TransactionCreateView.as_view(), name='transaction-create'),
]
