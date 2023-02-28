from django.shortcuts import render, HttpResponse

# Create your views here.
"""
html_cabecera = 
<h1>Mi Portafolio Personal</h1>
<ul>
    <li><a href="/">Inicio</a></li>
    <li><a href="/about">Acerca de Mi</a></li>
    <li><a href="/portfolio">Proyectos</a></li>
    <li><a href="/contact">Contacto</a></li>
</ul>
"""

def home(request):
    return render(request, 'core/home.html')

def base(request):
    return render(request, 'core/base.html')

def contact(request):
        return render(request, 'core/contact.html')                    
                                                