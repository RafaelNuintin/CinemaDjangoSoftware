from django.db import models

# Create your models here.
class Genero(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome do gênero")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"

class Filme(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome do filme")
    duracao = models.IntegerField(verbose_name = "Duração do filme")
    sinopse = models.CharField(max_length = 1000, verbose_name = "Sinopse")
    site_oficial = models.CharField(max_length = 100, verbose_name = "Site do filme")
    data_lancamento = models.DateField(verbose_name = "Data de lançamento")
    nota_avaliacao = models.FloatField(verbose_name = "Nota da avaliação")
    genero = models.ForeignKey(Genero, on_delete = models.CASCADE, verbose_name = "Gênero")
    pais = models.ForeignKey(Pais, on_delete = models.CASCADE, verbose_name = "País")
    diretor = models.ForeignKey(Diretor, on_delete = models.CASCADE, verbose_name = "Diretor")

    def __str__(self):
        return f"{self.nome}, {self.data_lancamento}"
    
    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"