from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wydatki/', views.lista_wydatkow, name='lista_wydatkow'),
    path('przychody/', views.lista_przychodow, name='lista_przychodow'),
]
    