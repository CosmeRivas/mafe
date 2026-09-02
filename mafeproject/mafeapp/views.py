from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import SolicitudCitaForm


def home(request):
    servicios = [
        {
            'icono': 'fa-passport',
            'titulo': 'Pasaportes',
            'descripcion': 'Tramitación y renovación de pasaportes para nacionales y extranjeros.',
        },
        {
            'icono': 'fa-stamp',
            'titulo': 'Visados',
            'descripcion': 'Gestión de visados de turismo, trabajo, estudio y reunificación familiar.',
        },
        {
            'icono': 'fa-id-card',
            'titulo': 'Residencias',
            'descripcion': 'Solicitud y renovación de permisos de residencia legal.',
        },
        {
            'icono': 'fa-file-invoice-dollar',
            'titulo': 'Registro en Impuestos',
            'descripcion': 'Registro y actualización ante el Ministerio de Hacienda / Impuestos.',
        },
        {
            'icono': 'fa-briefcase',
            'titulo': 'Carnet de Emprendedor',
            'descripcion': 'Tramitación del carnet de emprendedor para iniciar tu actividad económica.',
        },
        {
            'icono': 'fa-building',
            'titulo': 'Creación de Negocios',
            'descripcion': 'Asesoría integral para constituir y legalizar tu empresa.',
        },
    ]
    return render(request, 'mafeapp/home.html', {'servicios': servicios})


def nosotros(request):
    return render(request, 'mafeapp/nosotros.html')


def servicios(request):
    return render(request, 'mafeapp/servicios.html')


def contacto(request):
    if request.method == 'POST':
        form = SolicitudCitaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hemos recibido tu solicitud. Te contactaremos pronto para confirmar la cita.')
            return redirect('mafeapp:contacto')
    else:
        form = SolicitudCitaForm()
    return render(request, 'mafeapp/contacto.html', {'form': form})
