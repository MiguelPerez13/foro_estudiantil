from django.http import Http404
from django.shortcuts import render, redirect
from .models import *
from .forms import PostForm, RespuestaForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Count

def index(request):
    posts = Post.objects.select_related('categoria','carrera','autor')\
                        .annotate(num_respuestas=Count('respuestas'))\
                        .order_by('-fecha_creacion')
    context = {
        'posts' : posts,
        'section' : 'Recientes',
        'subtitle' : True,
    }
    return render(request,"index.html",context)

def categorias(request):
    try:
        categorias = Categoria.objects.annotate(num_post=Count('post')).order_by('nombre')
        context = {
            'categorias' : categorias
        }
    except Categoria.DoesNotExist:
        raise Http404("No existen categorias")
    return render(request,"categorias.html",context)

def categoria(request,categoria_id):
    try:
        categoria = Categoria.objects.get(pk=categoria_id)
        posts = Post.objects.filter(categoria=categoria_id)
        context = {
            'categoria' : categoria,
            'posts' : posts,
            'section' : categoria.nombre,
        }
    except Categoria.DoesNotExist:
        raise Http404("No existe la categoria")
    return render(request,"index.html",context)

def buscar_post(request):

    busqueda = request.GET.get('busqueda')
    categoria_id = request.GET.get('categoria')
    carrera_id = request.GET.get('carrera')

    queryset = Post.objects.select_related('categoria','carrera','autor')\
                        .annotate(num_respuestas=Count('respuestas'))\
                        .order_by('-fecha_creacion')

    if busqueda and busqueda.strip():
        queryset = queryset.filter(
            Q(titulo__icontains=busqueda) | Q(contenido__icontains=busqueda)
        )
    
    if categoria_id and categoria_id.isdigit():
        queryset = queryset.filter(categoria_id=categoria_id)
    
    if carrera_id and carrera_id.isdigit():
        queryset = queryset.filter(carrera_id=carrera_id)
    
    context = {
        'posts' : queryset,
        'section' : 'Busqueda',
        'subtitle' : True,
    }

    return render(request,'index.html',context)


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada para {username}! Ya puedes iniciar sesión.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

def carreras(request):
    try:
        carreras = Carrera.objects.annotate(num_post=Count('post')).order_by('nombre')
        context = {
            'carreras' : carreras
        }
    except Categoria.DoesNotExist:
        raise Http404("No existen carreras")
    return render(request,"carreras.html",context)

def carrera(request,carrera_id):
    try:
        carrera = Carrera.objects.get(pk=carrera_id)
        posts = Post.objects.filter(carrera=carrera_id)
        context = {
            'carrera' : carrera,
            'posts' : posts,
            'section' : carrera.nombre,
        }
    except Carrera.DoesNotExist:
        raise Http404("No existe la carrera")
    return render(request,"index.html",context)


@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
        # esto va para despues
        # post.author = request.user
        post.autor = User.objects.get(pk=2) # temporal
        post.save()
        post_id = request.GET.get('categ')
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

@login_required
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
        post = Post.objects.get(pk=post_id)
        context = {
            'form' : form,
            'post' : post,
        }
    return render(request,'respuesta.html',context)
