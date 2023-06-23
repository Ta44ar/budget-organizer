from django.shortcuts import render
from .models import Wydatek, Przychod

def home(request):
    return render(request, 'home_budget/base.html')

def lista_wydatkow(request):
    wydatki = Wydatek.objects.order_by('data_powstania')
    return render(request, 'home_budget/lista_wydatkow.html', {'wydatki': wydatki})

def lista_przychodow(request):
    przychody = Przychod.objects.order_by('data_powstania')
    return render(request, 'home_budget/lista_przychodow.html', {'przychody': przychody})
