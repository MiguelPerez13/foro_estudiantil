from datetime import date
from .models import Post, User, Respuesta, Categoria, Carrera
from django.db.models import Count


def foro_data(request):

    today = date.today()

    daily_activity = Post.objects.filter(fecha_creacion__date=today).count() + Respuesta.objects.filter(fecha_creacion__date=today).count()
    trending_posts = Post.objects.annotate(num_respuestas=Count('respuestas')).order_by('-num_respuestas')[:3]

    return{
        'total_post' : Post.objects.count(),
        'total_users' : User.objects.count(),
        'daily_activity' : daily_activity,
        'trending_posts' : trending_posts,
        'categorias' : Categoria.objects.all(),
        'carreras' : Carrera.objects.all(),
    }