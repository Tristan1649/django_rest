from rest_framework import serializers
from .models import Mersedes

class MersedesSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Mersedes
        fields = ('id', 'title', 'description', 'engine_displacement', 'sit_places', 'release', 'author')