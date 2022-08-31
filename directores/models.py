from django.db import models

# Create your models here.


class Peliculas(models.Model):
    titulo = models.CharField(
        max_length=64, help_text="Pon el título de la película")
    año_de_estreno = models.IntegerField()
    sinopsis = models.TextField(
        max_length=1000, help_text="Escribe la sinopsis de la película")
    dirigido_por = models.ForeignKey(
        'Directores', on_delete=models.SET_NULL, null=True, blank=True)
    urlImagen = models.URLField(default="https://kangsblackbeltacademy.com/wp-content/uploads/2017/04/default-image.jpg")

    def __str__(self):
        return self.titulo


class Directores(models.Model):
    nombre = models.CharField(
        max_length=64, help_text="Escribe el nombre del director")
    apellido = models.CharField(
        max_length=64, help_text="Escribe el apellido del director")
    fecha_de_nacimiento = models.DateField()
    peliculas_dirigidas = models.ManyToManyField('Peliculas', null=True, blank=True)
    nacionalidad = models.CharField(max_length=64, null=True, help_text="Pon la nacionalidad del director")
    urlImagen = models.URLField(default="https://kangsblackbeltacademy.com/wp-content/uploads/2017/04/default-image.jpg")

    def __str__(self):
        return "%s %s" % (self.nombre, self.apellido)