from django.forms import ModelForm, inlineformset_factory
from .models import Pojazd, Zdjecie

class PojazdForm(ModelForm):
    class Meta:
        model = Pojazd
        exclude = ['uzytkownik', 'data_dodania', 'data_publikacji', 'czy_usuniety']
        labels = {
            'czy_opublikowany': "Czy chcesz opublikować ofertę?"
        }

class ZdjecieForm(ModelForm):
    class Meta:
        model = Zdjecie
        fields = ['zdjecie', 'czy_glowny']

ZdjecieFormSet = inlineformset_factory(Pojazd, Zdjecie, ZdjecieForm, can_delete=False)
