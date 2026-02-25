from django.http import Http404
from django.shortcuts import render, redirect
from .models import *
from .forms import PostForm, RespuestaForm

def index(request):
    categorias = Categoria.objects.all().order_by('nombre')
    context = {
        'categorias' : categorias
    }
    return render(request,"index.html",context)

def categoria(request,categoria_id):
    try:
        categoria = Categoria.objects.get(pk=categoria_id)
        posts = Post.objects.filter(categoria=categoria_id)
        context = {
            'categoria' : categoria,
            'posts' : posts,
        }
    except Categoria.DoesNotExist:
        raise Http404("No existe la categoria")
    return render(request,"categoria.html",context)


def crear_post(request,categoria_id=None):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
        # esto va para despues
        # post.author = request.user
        post.autor = User.objects.get(pk=2) # temporal
        post.save()
        if categoria_id:
            return redirect('categoria',categoria_id=categoria_id)
        else:
            return redirect('index')
    else:
        form = PostForm()
    return render(request,'crear-post.html',{'form' : form})

def post(request,post_id):
    post = Post.objects.get(pk=post_id)
    respuestas = Respuesta.objects.filter(post=post_id)
    context = {
        'post' : post,
        'respuestas' : respuestas
    }
    return render(request,'post.html',context)

def crear_respuesta(request,post_id):
    if request.method == 'POST':
        form = RespuestaForm(request.POST)
        if form.is_valid():
            respuesta = form.save(commit=False)
            respuesta.post = Post.objects.get(pk=post_id)
            respuesta.autor = User.objects.get(pk=1) # temporal
            respuesta.save()
            return redirect('post',post_id)
    else:
        form = RespuestaForm()
    return render(request,'respuesta.html',{'form' : form})