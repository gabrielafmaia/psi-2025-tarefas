from django.shortcuts import render
from .models import Postagem, Blog

context = {
    "postagens": Postagem.objects.all(),
    "blogs": Blog.objects.all(),
}

def index(request):
    return render(request, 'blog/index.html', context)

def sobre(request):
    return render(request, 'blog/sobre.html', context)

def contato(request):
    return render(request, 'blog/contato.html', context)
