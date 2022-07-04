
from django.db import router
from django.urls import URLPattern
from rest_framework.routers import DefaultRouter
from .views import MersedesViewSet

router = DefaultRouter()
router.register('Mersedes', MersedesViewSet)

urlpatterns = router.urls