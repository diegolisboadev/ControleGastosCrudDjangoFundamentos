from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField('nome', max_length=100, null=False, blank=True)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Transacao(models.Model):
    data = models.DateTimeField() # auto_now=True
    descricao = models.CharField(max_length=200, null=True, blank=True)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    observacoes = models.TextField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Transações"

    def __str__(self):
        return self.descricao


