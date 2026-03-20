from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    data_publicacao = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT, related_name='livros', null=True, blank=True)

    def __str__(self):
        return self.titulo