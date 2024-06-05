from django.shortcuts import render

# def listmembres(request):
#     return render(request, 'bibliothecaire/index.html')

from bibliothecaire.models import Membre
from bibliothecaire.models import Media
from bibliothecaire.forms import Ajoutmembre
from bibliothecaire.forms import Ajoutmedia


# AFFICHAGE DE LA LISTE DES MEMBRES
def listmembres(request):
    membres = Membre.objects.all()
    return render(request, 'bibliothecaire/listmembres.html',
                  {'membres': membres})


# AFFICHAGE DE LA LISTE DES MEDIAS
def listmedias(request):
    medias = Media.objects.all()
    return render(request, 'bibliothecaire/listmedias.html',
                  {'medias': medias})


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
            return render(request, 'bibliothecaire/ajoutmembre.html',
                          {'membres': membres})
    else:
        ajoutmembre = Ajoutmembre()
        return render(request,
                      'bibliothecaire/ajoutmembre.html',
                      {'ajoutmembre': ajoutmembre}
                      )


# CREATION D'UN NOUVEAU MEDIA
def ajoutmedia(request):
    if request.method == 'POST':
        ajoutmedia = Ajoutmedia(request.POST)
        if ajoutmedia.is_valid():
            media = Media()
            media.category = ajoutmedia.cleaned_data['category'] 
            media.name = ajoutmedia.cleaned_data['name']
            media.save()
            medias = Media.objects.all()
            return render(request, 'bibliothecaire/ajoutmedia.html',
                          {'medias': medias})
    else:
        ajoutmedia = Ajoutmedia()
        return render(request,
                      'bibliothecaire/ajoutmedia.html',
                      {'ajoutmedia': ajoutmedia}
                      )