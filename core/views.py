from django.shortcuts import render
from .models import Dish


# Create your views here.
def index(request):
    # Demander directement tous les plats visibles de la catégorie 'PLAT'
    dishes = Dish.objects.filter(is_visible=True, category='PLAT')

    # Demander directement tous les plats visibles de la catégorie 'SOUPE'
    soups = Dish.objects.filter(is_visible=True, category='SOUPE')

    context = {
        'dishes': dishes,
        'soups': soups
    }
    return render(request, 'index.html', context)
