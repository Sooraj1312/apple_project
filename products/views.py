from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from users.permissions import IsAdmin
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.shortcuts import render, get_object_or_404
from .models import Product
from categories.models import Category 
from banners.models import Banner
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

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

class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "role": getattr(user, 'role', 'Customer')
        })

def category_products(request, cat_id):
    category = get_object_or_404(Category, id=cat_id)
    products = Product.objects.filter(category=category)
    
    return render(request, 'products/category_list.html', {
        'category': category, 
        'products': products
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product.html', {'product': product})

def store_page(request):
    banners = Banner.objects.filter(is_active=True).order_by('-created_at')
    products = Product.objects.all()
    
    return render(request, 'products/store.html', {'banners': banners, 'products': products})