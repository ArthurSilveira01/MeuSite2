from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    endereco = models.CharField(blank=True, null=True)
    data_de_nascimento = models.DateField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome}[{self.email}]'



# Create your models here.
