from django.shortcuts import render

def listmembres(request):
    return render(request, 'bibliothecaire/index.html')
