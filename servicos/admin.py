from django.contrib import admin

from servicos.models import (Orcamento, Atendimento, ProcedimentoEstetico,
                             TipoDiagnostico, TipoExame, TipoProcedimento,
                             ProcedimentoClinico, AtendimentoProcClinico,
                             AtendimentoProcEstetico, Autorizacao, Comissao,
                             DiagnosticoAnimal, Estadia, Exame, FeitoPor,
                             FichaDiagnostico, TipoStatusAtendimento,
                             TipoStatusEstadia, StatusAtendimento,
                             StatusEstadia)

# Register your models here.
admin.site.register(Orcamento)
admin.site.register(Atendimento)
admin.site.register(ProcedimentoEstetico)
admin.site.register(TipoDiagnostico)
admin.site.register(TipoExame)
admin.site.register(TipoProcedimento)
admin.site.register(ProcedimentoClinico)
admin.site.register(AtendimentoProcClinico)
admin.site.register(AtendimentoProcEstetico)
admin.site.register(Autorizacao)
admin.site.register(Comissao)
admin.site.register(DiagnosticoAnimal)
admin.site.register(Estadia)
admin.site.register(Exame)
admin.site.register(FeitoPor)
admin.site.register(FichaDiagnostico)
admin.site.register(TipoStatusAtendimento)
admin.site.register(TipoStatusEstadia)
admin.site.register(StatusAtendimento)
admin.site.register(StatusEstadia)
