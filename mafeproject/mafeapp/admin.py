from django.contrib import admin
from .models import SolicitudCita


@admin.register(SolicitudCita)
class SolicitudCitaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'telefono', 'servicio', 'fecha_preferida', 'hora_preferida', 'creada_en')
	list_filter = ('servicio', 'fecha_preferida')
	search_fields = ('nombre', 'telefono', 'correo')
