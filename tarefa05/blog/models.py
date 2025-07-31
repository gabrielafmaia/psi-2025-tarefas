from django.db import models

class Postagem(models.Model):
    imagem = models.ImageField(upload_to="imagem/")
    texto = models.CharField(max_length=2000)
    titulo = models.CharField(max_length=50)
    data_publicacao = models.DateField()

    def __str__(self):
        return f"{self.titulo} - {self.data_publicacao}"

    class Meta:
        verbose_name_plural = "Postagens"

class Blog(models.Model):
    titulo = models.CharField(max_length=100)
    copyright = models.CharField(max_length=50)
