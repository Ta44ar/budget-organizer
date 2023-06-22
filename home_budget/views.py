from django.shortcuts import render
from .models import wydatek, przychod

def lista_wydatkow(request):
    wydatki = wydatek.objects.all()
    return render(request, 'home_budget/lista_wydatkow.html', {'wydatki': wydatki})

def lista_przychodow(request):
    przychody = przychod.objects.all()
    return render(request, 'home_budget/lista_przychodow.html', {'przychody': przychody})
