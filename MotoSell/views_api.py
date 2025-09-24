from rest_framework import viewsets, permissions, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Pojazd
from .serializers import PojazdSerializer, RejestracjaSerializer
import datetime
from django.db.models import Q
from django.contrib.auth.models import User

class PojazdViewSet(viewsets.ModelViewSet):
    serializer_class = PojazdSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.action == 'moje_pojazdy' or self.action == 'publikuj' or self.action == "usun" or self.action == "update":
            return Pojazd.objects.filter(czy_usuniety=False, uzytkownik=self.request.user)
        elif self.action == 'retrieve':
            if self.request.user.is_authenticated:
                return Pojazd.objects.filter(Q(czy_usuniety=False) & (Q(czy_opublikowany=True) | Q(uzytkownik=self.request.user)))
            return Pojazd.objects.filter(czy_usuniety=False, czy_opublikowany=True)
        return Pojazd.objects.filter(czy_usuniety=False, czy_opublikowany=True)

    def perform_create(self, serializer):
        pojazd = serializer.save(uzytkownik=self.request.user)
        if pojazd.czy_opublikowany:
            pojazd.data_publikacji = datetime.date.today()
            pojazd.save()
    @action(detail=False, methods=['get'], url_path='moje', permission_classes=[permissions.IsAuthenticated])
    def moje_pojazdy(self, request):
        pojazdy = self.get_queryset()
        serializer = self.get_serializer(pojazdy, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], url_path='publikuj', permission_classes=[permissions.IsAuthenticated])
    def publikuj(self, request, pk=None):
        pojazd = self.get_object()
        pojazd.czy_opublikowany = True
        pojazd.data_publikacji = datetime.date.today()
        pojazd.save()
        return Response({"status": "opublikowany"})

    @action(detail=True, methods=['post'], url_path='cofnij_publikacje', permission_classes=[permissions.IsAuthenticated])
    def cofnij_publikacje(self, request, pk=None):
        pojazd = self.get_object()
        pojazd.czy_opublikowany = False
        pojazd.data_publikacji = None
        pojazd.save()
        return Response({"status": "cofnieto publikacje"})

    def perform_update(self, serializer):
        pojazd = serializer.save()
        if pojazd.czy_opublikowany and not pojazd.data_publikacji:
            pojazd.data_publikacji = datetime.date.today()
            pojazd.save()

    @action(detail=True, methods=['post'], url_path='usun', permission_classes=[permissions.IsAuthenticated])
    def usun(self, request, pk=None):
        pojazd = self.get_object()
        pojazd.czy_usuniety = True
        pojazd.save()
        return Response({"status": "usunieto oferte"})
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RejestracjaSerializer
    permission_classes = [permissions.AllowAny]
