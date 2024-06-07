from django.db import models
from django.db.models import F


#J'import ensuite le model Media de l'application membre dans l'application bibliotheque
# from membre.models import Media


# class Loan(models.Model):
    # media = models.ForeignKey(Media, null=True, on_delete=models.SET_NULL)
    # emprunteur = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    # date = models.DateField(null=True)


class Membre(models.Model):
    first_name = models.fields.CharField(max_length=50)
    last_name = models.fields.CharField(max_length=50)
    # email = models.EmailField(max_length=50)


class Media(models.Model):
    category = models.fields.CharField(max_length=100)
    name = models.fields.CharField(max_length=150)
    available = models.BooleanField(default=True)

