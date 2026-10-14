from rest_framework.routers import DefaultRouter
from .views import BannersViewset

router= DefaultRouter()
router.register('',BannersViewset, basename='banner')

urlpatterns = router.urls