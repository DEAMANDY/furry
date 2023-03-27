from django.urls import path
from . import views
from .views import index, Padopcion, Pubmascotas, dudas

urlpatterns = [
    path('', index),
    path('Adopcion/', Padopcion, name="Adopcion"),
    path('Dudas/', dudas, name="Dudas"),
    path('PublicarM/', Pubmascotas, name="Publicar_mascotas"),
    path('registrar/', views.registrar, name='registrar'),

]



