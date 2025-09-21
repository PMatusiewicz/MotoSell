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
        fields = ['zdjecie']

ZdjecieFormSet = inlineformset_factory(Pojazd, Zdjecie, ZdjecieForm, can_delete=False, extra=5, max_num=5, min_num=1)
