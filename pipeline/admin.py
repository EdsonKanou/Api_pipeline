from django.contrib import admin
from mon_api.models import Sensor  # Utilisez le modèle 'Sensor' (avec la première lettre en majuscule)

admin.site.register(Sensor)  # Enregistrez le modèle 'Sensor' dans l'interface d'administration
