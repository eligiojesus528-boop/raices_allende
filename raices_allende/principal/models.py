from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class LugarTuristico(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="lugares/", blank=True)
    ubicacion = models.CharField(max_length=300)
    video = models.URLField(blank=True)

    def __str__(self):
        return self.nombre


class Gastronomia(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="gastronomia/", blank=True)

    def __str__(self):
        return self.nombre


class Tradicion(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="tradiciones/", blank=True)

    def __str__(self):
        return self.nombre


class Artesania(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="artesanias/", blank=True)

    def __str__(self):
        return self.nombre


class CulturaAficion(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="cultura/", blank=True)

    def __str__(self):
        return self.nombre


class Galeria(models.Model):
    # Para saber a qué sección y a qué elemento pertenece cada foto
    seccion = models.CharField(max_length=50, choices=[
        ('lugares', 'Lugares Turísticos'),
        ('gastronomia', 'Gastronomía'),
        ('tradiciones', 'Tradiciones'),
        ('artesanias', 'Artesanías'),
    ])
    elemento_id = models.IntegerField(null=True,blank=True)
    imagen = models.ImageField(upload_to="galeria/")
    titulo = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.titulo or "Foto sin título"