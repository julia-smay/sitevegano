from django.db import models

class Restaurante(models.Model):

    OPCOES_CATEGORIA = [
        ("SELF SERVICE", "Self service"),
        ("BURGER", "Burger"),
        ("SUSHI", "Sushi"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    faixa_preco = models.CharField(max_length=100, null=True, blank=True)
    nota = models.CharField(max_length=10, blank=False, null=False)
    informacoes_adicionais = models.CharField(max_length=150, null=True, blank=True, default='')
    horario_funcionamento = models.CharField(max_length=150, null=True, blank=True)
    localizacao = models.CharField(max_length=150, null=False, blank=False)
    contato = models.CharField(max_length=150, null=True, blank=True)
    foto = models.ImageField(upload_to="fotos/", blank=True)

    def __str__(self):
        return self.nome