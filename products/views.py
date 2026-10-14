from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from users.permissions import IsAdmin
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset= Product.objects.all().order_by('-created_at')
    serializer_class= ProductSerializer
    
    filter_backends= [DjangoFilterBackend, OrderingFilter]
    filterset_fields= ['category','price']
    ordering_fields = ['price','created_at']
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdmin()]
        return [AllowAny()]
