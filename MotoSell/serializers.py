from rest_framework import serializers
from .models import Pojazd, Zdjecie

class ZdjecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zdjecie
        fields = '__all__'

class PojazdSerializer(serializers.ModelSerializer):
    zdjecia = ZdjecieSerializer(many=True, read_only=True, source="zdjecie_set")
    class Meta:
        model = Pojazd
        fields = '__all__'

