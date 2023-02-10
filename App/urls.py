from django.urls import path, include
from rest_framework import routers
from .views import TransactionViewSet, home

router = routers.DefaultRouter()
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('home/', home, name='home'),
]
