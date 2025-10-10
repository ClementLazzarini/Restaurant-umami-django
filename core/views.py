from django.shortcuts import render
from .models import Dish

import os
import subprocess
from django.http import HttpResponse
from django.conf import settings


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


def update_server(request):
    """
    Vue qui exécute un git pull et recharge le serveur web.
    """
    # Chemin vers la racine de votre projet
    project_root = settings.BASE_DIR

    # Commande 1 : Exécuter 'git pull'
    try:
        subprocess.check_output(['git', 'pull'], cwd=project_root, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return HttpResponse(f"Erreur lors du git pull:\n{e.output.decode()}", status=500)

    # Commande 2 : Recharger le serveur PythonAnywhere en "touchant" le fichier WSGI
    try:
        # Assurez-vous que ce chemin est correct (il l'est normalement)
        wsgi_file_path = f'/var/www/{os.environ.get("PYTHONANYWHERE_DOMAIN")}_wsgi.py'
        with open(wsgi_file_path, 'a'):
            os.utime(wsgi_file_path, None)
    except Exception as e:
        return HttpResponse(f"Erreur lors du rechargement du serveur:\n{str(e)}", status=500)

    return HttpResponse("Mise à jour réussie !")
