from django.urls import path

from . import views

urlpatterns = [
    path('peliculas/', views.listarPeliculas, name='peliculas'),
    path('directores/', views.listarDirectores, name='directores')
]