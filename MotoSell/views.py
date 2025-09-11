from django.contrib.auth import logout, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .forms import PojazdForm
from .models import Pojazd
import datetime

def index(request):
    uzytkownik = request.user
    return render(request, "MotoSell/index.html", {
        "uzytkownik": uzytkownik
    })

def rejestracja(request):
    if request.method == "POST":
        formularz_rejestracji = UserCreationForm(request.POST)
        if formularz_rejestracji.is_valid():
            nowy_uzytkownik = formularz_rejestracji.save()
            auth_login(request, nowy_uzytkownik)
            return redirect("index")
    else:
        formularz_rejestracji = UserCreationForm()

    return render(request, "MotoSell/rejestracja.html", {
        "formularz_rejestracji": formularz_rejestracji
    })

def login(request):
    if request.method == "POST":
        formularz_logowania = AuthenticationForm(data=request.POST)
        if formularz_logowania.is_valid():
            nowy_uzytkownik = formularz_logowania.get_user()
            auth_login(request, nowy_uzytkownik)
            return redirect("index")
    else:
        formularz_logowania = AuthenticationForm()

    return render(request, "MotoSell/login.html", {
        "formularz_logowania": formularz_logowania
    })


@login_required
def wyloguj(request):
    logout(request)
    return redirect("index")

@login_required
def kreator(request):
    if request.method == "POST":
        formularz_pojazdu = PojazdForm(request.POST, request.FILES)
        if formularz_pojazdu.is_valid():
            pojazd = formularz_pojazdu.save(commit=False)
            pojazd.uzytkownik = request.user
            if pojazd.czy_opublikowany:
                pojazd.data_publikacji = datetime.date.today()
            pojazd.save()
            return redirect("/pojazdy")
    else:
        formularz_pojazdu = PojazdForm()
    return render(request, "MotoSell/kreator.html", {
        "formularz_pojazdu": formularz_pojazdu
    })

def pojazdy(request):
    pojazdy_wszystkie = Pojazd.objects.filter()
    return render(request, "MotoSell/pojazdy.html", {
        "pojazdy_wszystkie": pojazdy_wszystkie
    })

@login_required
def moje_pojazdy(request):
    pojazdy_wszystkie = Pojazd.objects.filter()
    return render(request, "MotoSell/moje_pojazdy.html", {
        "pojazdy_wszystkie": pojazdy_wszystkie
    })

def oferta(request, pk):
    if request.user.is_authenticated:
        pojazd = get_object_or_404(Pojazd, Q(pk=pk) & Q(czy_usuniety=False) & (Q(czy_opublikowany=True) | Q(uzytkownik=request.user)))
    else:
        pojazd = get_object_or_404(Pojazd, pk=pk, czy_opublikowany=True, czy_usuniety=False)
    return render(request, "MotoSell/oferta.html",{
        "pojazd": pojazd
    })

@login_required
def publikuj(request, pk):
    pojazd = get_object_or_404(Pojazd, pk=pk, uzytkownik=request.user)
    pojazd.czy_opublikowany = True
    pojazd.data_publikacji = datetime.datetime.now()
    pojazd.save()
    return redirect("oferta", pk=pk)

@login_required
def cofnij_publikacje(request, pk):
    pojazd = get_object_or_404(Pojazd, pk=pk, uzytkownik=request.user)
    pojazd.czy_opublikowany = False
    pojazd.data_publikacji = None
    pojazd.save()
    return redirect("oferta", pk=pk)

@login_required
def usun(request, pk):
    pojazd = get_object_or_404(Pojazd, pk=pk, uzytkownik=request.user)
    pojazd.czy_usuniety = True
    pojazd.save()
    return redirect("moje_pojazdy")