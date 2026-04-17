import re

from django.db import models

from .categoria import Categoria
from .editora import Editora
from .autor import Autor


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    data_publicacao = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, 
        related_name='livros', 
        null=True, 
        blank=True)
    editora = models.ForeignKey(
        Editora, on_delete=models.PROTECT,
        related_name='livros',
        blank=True,
        null=True
    )
    autor = models.ManyToManyField(Autor, related_name='livros', blank=True)

    
    
    def __str__(self):
        return self.titulo