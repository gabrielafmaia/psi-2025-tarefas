from django.db import models

class Postagem(models.Model):
    imagem = models.ImageField(upload_to="imagem/")
    texto = models.CharField()
    titulo = models.CharField(max_length=200)
    data_publicacao = models.DateField(max_length=10000)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Postagens"

class Blog(models.Model):
    titulo = models.CharField(max_length=50)
    copyright = models.CharField(max_length=100)

    def __str__(self):
            return self.titulo