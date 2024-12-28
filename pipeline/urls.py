from django.contrib import admin
from django.urls import path
from pipeline import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("iot/", views.liste, name='list'),  # Vue pour récupérer la liste des capteurs
    path("iot/<int:id>/", views.uni, name='uni'),  # Vue pour récupérer un capteur spécifique par ID
]
