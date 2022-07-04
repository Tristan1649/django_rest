from rest_framework.viewsets import ModelViewSet
from .models import Mersedes
from .serializers import MersedesSerilizer

class MersedesViewSet(ModelViewSet):
    queryset = Mersedes.objects.all()
    serialize_class = MersedesSerilizer

