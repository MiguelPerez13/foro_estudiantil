from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("categoria/<int:categoria_id>",views.categoria,name="categoria"),
    path("post/crear/<int:categoria_id>",views.crear_post,name="crear-post"),
    path("post/<int:post_id>",views.post,name="post"),
    path("post/respuesta/<int:post_id>",views.crear_respuesta,name="respuesta"),
]