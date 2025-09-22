from rest_framework import viewsets
from .models import Pojazd
from .serializers import PojazdSerializer

class PojazdViewSet(viewsets.ModelViewSet):
    queryset = Pojazd.objects.filter(czy_usuniety=False)
    serializer_class = PojazdSerializer