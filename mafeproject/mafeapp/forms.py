from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import SolicitudCita


class SolicitudCitaForm(forms.ModelForm):
    class Meta:
        model = SolicitudCita
        fields = ('nombre', 'telefono', 'correo', 'servicio', 'fecha_preferida', 'hora_preferida', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Tu nombre completo'}),
            'telefono': forms.TelInput(attrs={'placeholder': '+240 ...'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'tu@correo.com'}),
            'servicio': forms.Select(choices=[
                ('', 'Selecciona un servicio'),
                ('Gestión administrativa y documental', 'Gestión administrativa y documental'),
                ('Registro civil y certificaciones', 'Registro civil y certificaciones'),
                ('Gestión fiscal y financiera', 'Gestión fiscal y financiera'),
                ('Cumplimiento laboral y personal', 'Cumplimiento laboral y personal'),
                ('Inmigración y extranjería', 'Inmigración y extranjería'),
                ('Registros y trámites empresariales', 'Registros y trámites empresariales'),
                ('Otro servicio', 'Otro servicio'),
            ]),
            'fecha_preferida': forms.DateInput(attrs={'type': 'date'}),
            'hora_preferida': forms.TimeInput(attrs={'type': 'time', 'min': '10:00', 'max': '17:00'}),
            'mensaje': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Cuéntanos brevemente cómo podemos ayudarte'}),
        }

    def clean_fecha_preferida(self):
        fecha = self.cleaned_data['fecha_preferida']
        if fecha < timezone.localdate():
            raise ValidationError('Selecciona una fecha futura.')
        if fecha.weekday() > 4:
            raise ValidationError('Las citas están disponibles de lunes a viernes.')
        return fecha

    def clean_hora_preferida(self):
        hora = self.cleaned_data['hora_preferida']
        if not (hora.hour >= 10 and hora.hour < 17):
            raise ValidationError('Selecciona una hora entre las 10:00 y las 17:00.')
        return hora