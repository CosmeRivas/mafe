from django.shortcuts import render


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
