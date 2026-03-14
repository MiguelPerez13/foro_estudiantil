from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("categoria/<int:categoria_id>",views.categoria,name="categoria"),
    path("categorias/",views.categorias,name="categorias"),
    path("carreras/",views.carreras,name="carreras"),
    path("post/crear/",views.crear_post,name="crear-post"),
    path("post/<int:post_id>",views.post,name="post"),
    path("post/respuesta/<int:post_id>",views.crear_respuesta,name="respuesta"),
    path("post/buscar/",views.buscar_post,name="busqueda"),
    path('registro/', views.registro, name='registro'),
]