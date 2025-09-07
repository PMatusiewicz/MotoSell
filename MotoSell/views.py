from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
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
            login(request, nowy_uzytkownik)
            return redirect('index')
    else:
        formularz_rejestracji = UserCreationForm()

    return render(request, "MotoSell/rejestracja.html", {
        "formularz_rejestracji": formularz_rejestracji
    })