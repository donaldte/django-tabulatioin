from django.contrib import admin
from .models import Auteur, Livre
class LivreInline(admin.TabularInline):
    model = Livre
    extra = 1  # Vous pouvez spécifier combien de formulaires vides sont affichés par défaut.

class AuteurAdmin(admin.ModelAdmin):
    inlines = [LivreInline]

admin.site.register(Auteur, AuteurAdmin)
