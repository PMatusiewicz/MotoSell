from django.contrib.auth import logout, login as auth_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

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
            return redirect('index')
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
            return redirect('index')
    else:
        formularz_logowania = AuthenticationForm()

    return render(request, "MotoSell/login.html", {
        "formularz_logowania": formularz_logowania
    })

def wyloguj(request):
    logout(request)
    return redirect('index')
