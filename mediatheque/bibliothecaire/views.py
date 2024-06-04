from django.shortcuts import render

# def listmembres(request):
#     return render(request, 'bibliothecaire/index.html')

from bibliothecaire.models import Membre
from bibliothecaire.forms import Ajoutmembre

# AFFICHAGE DE LA LISTE DES MEMBRES
def listmembres(request):
    membres = Membre.objects.all()
    return render(request, 'bibliothecaire/index.html',
                  {'membres': membres})

# CREATION D'UN NOUVEAU MEMBRE
def ajoutmembre(request):
    if request.method == 'POST':
        ajoutmembre = Ajoutmembre(request.POST)
        if ajoutmembre.is_valid():
            membre = Membre()
            membre.first_name = ajoutmembre.cleaned_data['first_name']
            membre.last_name = ajoutmembre.cleaned_data['last_name']
            membre.save()
            membres = Membre.objects.all()
            return render(request, 'bibliothecaire/index.html',
                          {'membres': membres})
    else:
        ajoutmembre = Ajoutmembre()
        return render(request,
                      'bibliothecaire/ajoutmembre.html',
                      {'ajoutmembre': ajoutmembre}
                      )
