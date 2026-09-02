from django.db import models


class SolicitudCita(models.Model):
	nombre = models.CharField(max_length=120)
	telefono = models.CharField(max_length=30)
	correo = models.EmailField()
	servicio = models.CharField(max_length=100)
	fecha_preferida = models.DateField()
	hora_preferida = models.TimeField()
	mensaje = models.TextField(blank=True)
	creada_en = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'solicitud de cita'
		verbose_name_plural = 'solicitudes de cita'
		ordering = ['-creada_en']

	def __str__(self):
		return f'{self.nombre} - {self.fecha_preferida}'
