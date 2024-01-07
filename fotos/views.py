from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from random import sample
from .models import Foto


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
        nomes_escolhidos.append(str(foto.foto)[31:])
        ids_escolhidos.append(str(foto.id))
                
    context = {
        'desenho': desenho,
        'fotos_escolhidas': ' '.join(nomes_escolhidos),
        'ids_escolhidos': ' '.join(ids_escolhidos)
    }
    return render(request, 'index.html', context=context)


def mensagem(request, foto_id):
    foto = get_object_or_404(Foto, pk=foto_id)

    context = {'foto': str(foto.foto)[16:],
               'titulo': foto.titulo,
               'texto': foto.texto,
               'id': foto.id}
    return render(request, 'mensagem.html', context=context)
