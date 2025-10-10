from django.shortcuts import render
from .models import Dish

import os
import subprocess
import requests

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
    """
    Vue qui exécute un git pull et recharge le serveur web.
    """
    # Chemin vers la racine de votre projet
    project_root = settings.BASE_DIR
    try:
        subprocess.check_output(['git', 'pull'], cwd=project_root, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return HttpResponse(f"Erreur lors du git pull:\n{e.output.decode()}", status=500)

    # --- PARTIE 2 : RELOAD VIA L'API (modifiée) ---
    try:
        username = os.environ.get("PYTHONANYWHERE_USER", "ClemLazzTech")
        domain_name = os.environ.get("PYTHONANYWHERE_DOMAIN", "clemlazztech.pythonanywhere.com")

        # <-- CORRECTION ICI : On lit la clé depuis les settings
        api_token = settings.PA_API_TOKEN

        response = requests.post(
            f'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain_name}/reload/',
            headers={'Authorization': f'Token {api_token}'}
        )

        if response.status_code == 200:
            return HttpResponse("Mise à jour et reload réussis via local_settings !")
        else:
            return HttpResponse(f"Erreur lors du reload via API: {response.status_code} - {response.text}", status=500)

    except Exception as e:
        return HttpResponse(f"Erreur inattendue lors du reload:\n{str(e)}", status=500)
