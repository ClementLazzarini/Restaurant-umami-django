from django.shortcuts import render
from .models import Dish

import os
import subprocess

from django.http import HttpResponse
from django.conf import settings


from django.views.decorators.csrf import csrf_exempt


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


@csrf_exempt
def update_server(request):
    project_root = settings.BASE_DIR
    try:
        output = subprocess.check_output(['git', 'pull'], cwd=project_root, stderr=subprocess.STDOUT)
        # On ne fait plus que le git pull, on retire la partie reload
        return HttpResponse(f"Mise à jour via git pull réussie !\n\n{output.decode()}")

    except Exception as e:
        return HttpResponse(f"Erreur lors du git pull:\n{str(e)}", status=500)
