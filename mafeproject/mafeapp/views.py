from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import SolicitudCitaForm


def home(request):
    servicios = [
        {
            'icono': 'fa-passport',
            'titulo': 'Gestión Administrativa y Documental',
            'descripcion': '',
        },
        {
            'icono': 'fa-stamp',
            'titulo': 'Registro Civil y Certificaciones',
            'descripcion': 'Gestión de visados de turismo, trabajo, estudio y reunificación familiar.',
        },
        {
            'icono': 'fa-id-card',
            'titulo': '- Gestión Fiscal y Financiera',
            'descripcion': 'Solicitud y renovación de permisos de residencia legal.',
        },
        {
            'icono': 'fa-file-invoice-dollar',
            'titulo': '- Cumplimiento Laboral y Nóminas',
            'descripcion': 'Registro y actualización ante el Ministerio de Hacienda / Impuestos.',
        },
        {
            'icono': 'fa-briefcase',
            'titulo': '- Servicios de Extranjería e Inmigración',
            'descripcion': 'Tramitación del carnet de emprendedor para iniciar tu actividad económica.',
        },
        {
            'icono': 'fa-building',
            'titulo': 'Trámites Empresariales y Licencias',
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
