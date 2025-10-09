from django.contrib import admin
from .models import Dish


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    # On ajoute 'category' et 'is_star' pour les voir dans la liste
    list_display = ('name', 'price', 'category', 'is_star', 'is_visible')
    # On peut maintenant filtrer par ces nouveaux champs
    list_filter = ('category', 'is_star', 'is_visible')
    search_fields = ('name', 'description')
