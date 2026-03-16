from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100) # Ej: "Programación", "Cálculo"
    descripcion = models.TextField(blank=True)

    def __clase__(self):
        return self.nombre
    def __str__(self):
        return self.nombre

class Carrera(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE)
    archivo_adjunto = models.FileField(upload_to='tareas/', blank=True, null=True)

    def __str__(self):
        return self.titulo

class Respuesta(models.Model):
    post = models.ForeignKey(Post, related_name='respuestas', on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    es_solucion = models.BooleanField(default=False)

    def __str__(self):
        return self.contenido