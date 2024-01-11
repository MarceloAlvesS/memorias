from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Pagina

def home(request):
    paginas = Pagina.objects.all()
    context = {
        'paginas': paginas
    }
    
    return render(request, 'diario.html', context=context)


def pagina(request, pagina_id):
    pagina = get_object_or_404(Pagina, pk=pagina_id)
    context = {
        'pagina': pagina
    }

    return render(request, 'pagina.html', context=context)
