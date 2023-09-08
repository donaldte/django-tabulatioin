from django.db import models

class Auteur(models.Model):
    nom = models.CharField(max_length=100)

class Livre(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
