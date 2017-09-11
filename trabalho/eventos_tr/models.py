from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length = 150)
    email = models.CharField(max_length = 100)

    def __str__(self):
        return self.nome

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length = 12)

class PessoaJuridica(Pessoa):
    cnpj = models.CharField(max_length = 20)
    razaoSocial = models.CharField(max_length = 50)

class Autor(Pessoa):
    curriculo = models.CharField(max_length = 200)
    artigos = []

class Evento(models.Model):
    nome = models.CharField(max_length = 100)
    eventoPrincipal = models.CharField(max_length = 150)
    sigla = models.CharField(max_length = 10)
    dataEHoraDeInicio = models.DateTimeField(max_length = 10)
    palavrasChave = models.CharField(max_length = 100)
    logotipo = models.CharField(max_length = 50)
    realizador = models.ForeignKey(Pessoa, related_name = 'Pessoa', null = True, blank = False)
    cidade = models.CharField(max_length = 100)
    uf = models.CharField(max_length = 10)
    endereco = models.CharField(max_length = 150)
    cep = models.CharField(max_length = 15)

    def __str__(self):
        return self.nome

class EventoCientifico(Evento):
    issn = models.CharField(max_length = 100)

class ArtigoCientifico(models.Model):
    titulo = models.CharField(max_length = 110)
    autores = [Autor]
    evento = models.ForeignKey(EventoCientifico, related_name = 'EventoCientifico', null = True, blank = False)

    def __str__(self):
        return self.titulo

# Create your models here.
