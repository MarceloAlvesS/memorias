from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest
from random import sample
from .models import Foto
from django.urls import reverse


def index(request):
    desenho = [
    ' ** **',
    '*******',
    ' *****',
    '  ***',
    '   *'
]
    quantidade = ''.join(desenho).count('*')
    fotos_escolhidas = sample(list(Foto.objects.all()), k=quantidade)

    ids_escolhidos = []
    nomes_escolhidos = []
    for foto in fotos_escolhidas:
        nomes_escolhidos.append(str(foto.foto)[14:])
        ids_escolhidos.append(str(foto.id))

    context = {
        'desenho': desenho,
        'fotos_escolhidas': ' '.join(nomes_escolhidos),
        'ids_escolhidos': ' '.join(ids_escolhidos)
    }
    return render(request, 'index.html', context=context)


def mensagem(request, foto_id):
    foto = get_object_or_404(Foto, pk=foto_id)

    context = {'foto': str(foto.foto)[14:],
               'titulo': foto.titulo,
               'texto': foto.texto,
               'id': foto.id}
    return render(request, 'mensagem.html', context=context)

def editar(request, foto_id):
    if request.method == 'POST':
        titulo = request.POST.get('titulo', None)
        texto = request.POST.get('texto', None)
        foto = get_object_or_404(Foto, pk=foto_id)
        foto.titulo = titulo
        foto.texto = texto
        foto.save()
        return redirect('index')
    
    if request.method == 'GET':
        foto = get_object_or_404(Foto, pk=foto_id)

        context = {'foto': str(foto.foto)[14:],
                'titulo': foto.titulo,
                'texto': foto.texto,
                'id': foto.id}
        return render(request, 'editar.html', context=context)
    

def deletar(request, foto_id):
    return HttpResponse(f'olá mundo {foto_id}')

def admin(request, foto_id):
    return HttpResponse(f'olá mundo {foto_id}')

