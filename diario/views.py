from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Pagina

def home(request):
    paginas = Pagina.objects.all()
    context = {
        'paginas': paginas,
    }

    return render(request, 'diario.html', context=context)


def pagina(request, pagina_id):
    pagina = get_object_or_404(Pagina, pk=pagina_id)
    context = {
        'pagina': pagina,
    }

    return render(request, 'pagina.html', context=context)


def editar(request, pagina_id):
    pagina = get_object_or_404(Pagina, pk=pagina_id)
    if request.method == 'POST':
        pagina.titulo = request.POST.get('titulo', None)
        pagina.periodo_inicial = request.POST.get('periodo_inicial', None)
        pagina.periodo_final = request.POST.get('periodo_final', None)
        if not pagina.periodo_final:
            pagina.periodo_final = pagina.periodo_inicial
        pagina.texto = request.POST.get('texto', None)
        pagina.save()
        return redirect('diario')
    context = {
        'pagina': pagina,
        'tipo': 'editar'
    }

    return render(request, 'pagina_form.html', context=context)


def deletar(request, pagina_id):
    pagina = get_object_or_404(Pagina, pk=pagina_id)
    pagina.delete()
    return redirect('diario')


def criar(request):
    if request.method == 'POST':
        pagina = Pagina()
        pagina.titulo = request.POST.get('titulo', None)
        pagina.periodo_inicial = request.POST.get('periodo_inicial', None)
        pagina.periodo_final = request.POST.get('periodo_final', None)
        if not pagina.periodo_final:
            pagina.periodo_final = pagina.periodo_inicial
        pagina.texto = request.POST.get('texto', None)
        pagina.save()
        return redirect('diario')
    context = {
        'tipo': 'criar'
    }

    return render(request, 'pagina_form.html', context=context)