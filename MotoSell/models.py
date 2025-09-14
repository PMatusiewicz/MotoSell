from django.db import models
from django.contrib.auth.models import User

class Pojazd(models.Model):
    KATEGORIE = {
        "motocykl": "Motocykl",
        "osobowy": "Osobowy",
        "ciezarowy": "Ciężarowy"
    }
    PALIWO = {
        "benzyna": "Benzyna",
        "diesel": "Diesel",
        "lpg": "LPG"
    }

    tytul = models.CharField(max_length=100)
    opis = models.TextField()
    kategoria = models.CharField(max_length=10, choices=KATEGORIE.items())
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    rok_produkcji = models.PositiveIntegerField()
    przebieg = models.PositiveIntegerField()
    pojemnosc_skokowa = models.PositiveIntegerField()
    rodzaj_paliwa = models.CharField(max_length=10, choices=PALIWO.items())
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    zdjecie = models.ImageField(upload_to="zdjecia")
    data_dodania = models.DateField(auto_now_add=True)
    data_publikacji = models.DateField(null=True, blank=True)
    czy_opublikowany = models.BooleanField(default=False)
    czy_usuniety = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk}. {self.uzytkownik.username} {self.marka} {self.model}"

class Zdjecie(models.Model):
    zdjecie = models.ImageField(upload_to="zdjecia")

    def __str__(self):
        return f"{self.zdjecie}"

class Pivot(models.Model):
    zdjecie = models.ForeignKey(Zdjecie, on_delete=models.CASCADE)
    pojazd = models.ForeignKey(Pojazd, on_delete=models.CASCADE)
    czy_glowne = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.zdjecie} - {self.pojazd}"
