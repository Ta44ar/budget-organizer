from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wydatki/', views.lista_wydatkow, name='lista_wydatkow'),
    path('przychody/', views.lista_przychodow, name='lista_przychodow'),
    path('dodaj_wydatek/', views.dodaj_wydatek, name='dodaj_wydatek'),
    path('dodaj_przychod/', views.dodaj_przychod, name='dodaj_przychod'),
    path('zestawienie/', views.zestawienie, name='zestawienie'),
]

    