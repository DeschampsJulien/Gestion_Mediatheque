from django.shortcuts import render

# def index(request):
#     return render(request, 'membre/index.html')

from membre.models import Media

def listmedias(request):
    medias = Media.objects.all()
    return render(request, 'membre/index.html',
                  {'medias': medias})
