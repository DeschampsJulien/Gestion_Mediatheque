from django.urls import path
from membre import views

urlpatterns = [
    path('', views.listmedias, name="listmedias"),
]