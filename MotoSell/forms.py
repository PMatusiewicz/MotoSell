from django.forms import ModelForm
from .models import Pojazd, Zdjecie

class PojazdForm(ModelForm):
    class Meta:
        model = Pojazd
        exclude = ['uzytkownik', 'data_dodania', 'data_publikacji', 'czy_usuniety']
        labels = {
            'czy_opublikowany': "Czy chcesz opublikować ofertę?"
        }