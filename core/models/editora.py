import re

from django.db import models

class Editora(models.Model):
    nome = models.CharField(max_length=255)
    url = models.URLField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.nome