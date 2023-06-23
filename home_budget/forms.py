from django import forms
from .models import Wydatek, Przychod

class wydatekForm(forms.ModelForm):
    class Meta:
        model = Wydatek
        fields = ['nazwa', 'kwota', 'data_powstania']