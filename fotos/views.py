from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest
from random import sample
from .models import Foto


def home_redirect(request):
    return redirect('index')


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
    fotos_escolhidas = {
        'foto': [f'{foto.foto}'[14:] for foto in fotos_escolhidas],
        'id': [f'{foto.id}' for foto in fotos_escolhidas]
        }

    context = {
        'desenho': desenho,
        'fotos_escolhidas': ' '.join(fotos_escolhidas['foto']),
        'ids_escolhidos': ' '.join(fotos_escolhidas['id'])
    }
    return render(request, 'index.html', context=context)


def mensagem(request, foto_id):
    foto = get_object_or_404(Foto, pk=foto_id)
    context = {'foto': str(foto.foto)[14:],
               'titulo': foto.titulo,
               'texto': foto.texto,
               'id': foto.id,
               'anterior': request.META['HTTP_REFERER']
    }
    return render(request, 'mensagem.html', context=context)

def editar(request, foto_id):
    if request.method == 'POST':
        foto = get_object_or_404(Foto, pk=foto_id)
        foto.titulo = request.POST.get('titulo', None)
        foto.texto = request.POST.get('titulo', None)
        foto.save()
        return redirect('admin')
    
    if request.method == 'GET':
        foto = get_object_or_404(Foto, pk=foto_id)

        context = {'foto': str(foto.foto)[14:],
                'titulo': foto.titulo,
                'texto': foto.texto,
                'id': foto.id,
                'tipo': 'editar'
                }
        return render(request, 'editar.html', context=context)
    

def admin(request):
    context = {
        'fotos': sorted(Foto.objects.all(), key=lambda obj: obj.titulo)
    }
    return render(request, 'admin.html', context=context)


def criar(request):
    if request.method == 'POST':
        foto = Foto()
        foto.titulo = request.POST.get('titulo', None)
        foto.texto = request.POST.get('texto', None)
        foto.save()
        return redirect('admin')
    if request.method == 'GET':
        context = {
            'tipo': 'criar'
        }
        return render(request, 'editar.html', context=context)
