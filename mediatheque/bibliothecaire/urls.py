from django.urls import path
from bibliothecaire import views

urlpatterns = [
    path('', views.listmembres, name="listmembres"),
]