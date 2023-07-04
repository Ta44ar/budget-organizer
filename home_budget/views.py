from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.utils import timezone
from .models import Wydatek, Przychod
from .forms import WydatekForm, PrzychodForm

def home(request):
    return render(request, 'home_budget/base.html')

def lista_wydatkow(request):
    wydatki = Wydatek.objects.order_by('data_powstania')
    return render(request, 'home_budget/lista_wydatkow.html', {'wydatki': wydatki})

def lista_przychodow(request):
    przychody = Przychod.objects.order_by('data_powstania')
    return render(request, 'home_budget/lista_przychodow.html', {'przychody': przychody})

def dodaj_wydatek(request):
    if request.method == "POST":
        form = WydatekForm(request.POST)
        if form.is_valid():
            wydatek = form.save(commit=False)
            wydatek.autor = request.user
            wydatek.data_powstania = timezone.now()
            wydatek.save()
            return redirect('lista_wydatkow')
    else:
        form = WydatekForm()
    return render(request, 'home_budget/dodaj_wydatek.html', {'form': form})

def dodaj_przychod(request):
    if request.method == "POST":
        form = PrzychodForm(request.POST)
        if form.is_valid():
            przychod = form.save(commit=False)
            przychod.autor = request.user
            przychod.data_powstania = timezone.now()
            przychod.save()
            return redirect('lista_przychodow')
    else:
        form = PrzychodForm()
    return render(request, 'home_budget/dodaj_przychod.html', {'form': form})

def zestawienie(request):
    wydatki = Wydatek.objects.all()
    przychody = Przychod.objects.all()
    return render(request, 'home_budget/zestawienie.html', {'wydatki': wydatki, 'przychody': przychody})