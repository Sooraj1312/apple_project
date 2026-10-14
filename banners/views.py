from rest_framework import viewsets
from .models import Banner
from .serializers import BannerSerializer
from users.permissions import IsAdmin
from rest_framework.permissions import AllowAny


# Create your views here.
class BannersViewset(viewsets.ModelViewSet):
    serializer_class= BannerSerializer
    
    def get_queryset(self):
        if self.request.user.is_authenticated and hasattr(self.request.user, 'role') and self.request.user.role == 'admin':
            return Banner.objects.all().order_by('-created_at')
        
        return Banner.objects.filter(is_active=True).order_by('-created_at')
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdmin()]
        return [AllowAny()]