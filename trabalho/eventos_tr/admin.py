from django.contrib import admin

from eventos_tr.models import Pessoa, PessoaFisica, PessoaJuridica, Autor, Evento, EventoCientifico, ArtigoCientifico

admin.site.register(Pessoa)
admin.site.register(PessoaFisica)
admin.site.register(PessoaJuridica)
admin.site.register(Autor)
admin.site.register(Evento)
admin.site.register(EventoCientifico)
admin.site.register(ArtigoCientifico)


# Register your models here.
