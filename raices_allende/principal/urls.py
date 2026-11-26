from django.urls import path
from . import views

app_name = 'principal'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('lugares/', views.lugares, name='lugares'),
    path('gastronomia/', views.gastronomia, name='gastronomia'),
    path('tradiciones/', views.tradiciones, name='tradiciones'),
    path('artesanias/', views.artesanias, name='artesanias'),
    path('historia/', views.historia, name='historia'),
    path('contacto/', views.contacto, name='contacto'),
]