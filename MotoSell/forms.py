from django.forms import ModelForm
from .models import Pojazd

class PojazdForm(ModelForm):
    class Meta:
        model = Pojazd
        exclude = ['uzytkownik', 'data_dodania', 'data_publikacji', 'czy_usuniety']
        labels = {
            'czy_opublikowany': "Czy chcesz odrazu opublikować ofertę?"
        }