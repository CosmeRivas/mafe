from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import SolicitudCitaForm


def home(request):
    servicios = [
        {
            'icono': 'fa-passport',
            'titulo': 'Gestión Administrativa y Documental',
            'descripcion': 'Gestión y seguimiento de trámites administrativos y documentación personal o empresarial.',
        },
        {
            'icono': 'fa-stamp',
            'titulo': 'Registro Civil y Certificaciones',
            'descripcion': ' Solicitud y gestión de certificados y documentos oficiales del Registro Civil',
        },
        {
            'icono': 'fa-id-card',
            'titulo': 'Gestión Fiscal y Financiera',
            'descripcion': 'Asesoramiento y gestión de obligaciones fiscales, tributarias y financieras',
        },
        {
            'icono': 'fa-file-invoice-dollar',
            'titulo': 'Cumplimiento Laboral y Nóminas',
            'descripcion': ' Gestión de nóminas, obligaciones laborales y trámites ante los organismos correspondientes.',
        },
        {
            'icono': 'fa-briefcase',
            'titulo': 'Servicios de Extranjería e Inmigración',
            'descripcion': 'Asesoramiento y gestión de permisos de residencia, trabajo y otros trámites migratorios.',
        },
        {
            'icono': 'fa-building',
            'titulo': 'Trámites Empresariales y Licencias',
            'descripcion': 'Asesoría para constituir, regularizar y gestionar tu empresa y sus licencias.',
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
