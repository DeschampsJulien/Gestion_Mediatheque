from django.urls import path
from bibliothecaire import views

urlpatterns = [
    path('', views.listmembres, name="listmembres"),
    path('ajoutmembre/', views.ajoutmembre, name="ajoutmembre"),
    path('listmedias/', views.listmedias, name="listmedias"),
    path('ajoutmedia/', views.ajoutmedia, name="ajoutmedia"),
]