from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Pojazd, Zdjecie

class ZdjecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zdjecie
        fields = '__all__'

class PojazdSerializer(serializers.ModelSerializer):
    zdjecia = ZdjecieSerializer(many=True, read_only=True, source="zdjecie_set")
    class Meta:
        model = Pojazd
        exclude = ['uzytkownik', 'data_dodania', 'data_publikacji', 'czy_usuniety']

class RejestracjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        uzytkownik = User.objects.create_user(**validated_data)
        return uzytkownik
