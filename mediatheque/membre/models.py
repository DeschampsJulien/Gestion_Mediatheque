from django.db import models

class Media(models.Model):
    category = models.fields.CharField(max_length=100)
    name = models.fields.CharField(max_length=150)
    available = models.BooleanField(default=True)

# class livre(models.Model):
#     name = models.fields.CharField(max_length=150)
#     auteur = models.fields.CharField(max_length=150)
#     dateEmprunt = models.DateField(null=True, blank=True)
#     disponible = models.BooleanField('Disponible', default=True)
#     emprunteur = ""
#
# class dvd(models.Model):
#     name = models.fields.CharField(max_length=150)
#     realisateur = models.fields.CharField(max_length=150)
#     dateEmprunt = models.DateField(null=True, blank=True)
#     disponible = models.BooleanField('Disponible', default=True)
#     emprunteur = ""
#
# class cd(models.Model):
#     name = models.fields.CharField(max_length=150)
#     artiste = models.fields.CharField(max_length=150)
#     dateEmprunt = models.DateField(null=True, blank=True)
#     disponible = models.BooleanField('Disponible', default=True)
#     emprunteur = ""
#
# class jeuDePlateau(models.Model):
#     name = models.fields.CharField(max_length=150)
#     createur = models.fields.CharField(max_length=150)

