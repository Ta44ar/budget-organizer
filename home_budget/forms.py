from django import forms
from .models import Wydatek, Przychod

class WydatekForm(forms.ModelForm):
    class Meta:
        model = Wydatek
        fields = ['nazwa', 'kwota', 'data_powstania']

class PrzychodForm(forms.ModelForm):
    class Meta:
        model = Przychod
        fields = ['nazwa', 'kwota', 'data_powstania']