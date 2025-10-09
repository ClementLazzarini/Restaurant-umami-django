from django.db import models


class Dish(models.Model):
    DISH = 'PLAT'
    SOUP = 'SOUPE'

    CATEGORY_CHOICES = [
        (DISH, 'Plat'),
        (SOUP, 'Soupe'),
    ]

    name = models.CharField("Nom", max_length=200)
    korean_name = models.CharField("Nom Coréen", max_length=200)
    description = models.TextField("Description", blank=True)
    price = models.DecimalField("Prix", max_digits=5, decimal_places=2)
    category = models.CharField("Catégorie", max_length=10, choices=CATEGORY_CHOICES, default=DISH)
    is_star = models.BooleanField(
        "Plat à la une",
        default=False,
        help_text="Cochez pour afficher ce plat sur la page d'accueil."
    )
    is_visible = models.BooleanField("Visible sur le site", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Plat"
        verbose_name_plural = "Plats"
        ordering = ['-created_at']
